#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (C) 2010 - 2011, University of New Orleans
#
# This program is free software; you can redistribute it and/or modify it under
# the terms of the GNU General Public License as published by the Free
# Software Foundation; either version 2 of the License, or (at your option)
# any later version.
#
# Please read the COPYING file.
#
# --
#
# Server core. This program runs the server and starts listening the domain
# socket for requests. Handles and respondes to incoming requests.
#
# executers dictionary in ProcessRequest class contains the available
# requests.
#

# standard python modules
import os
from stat import S_IRWXU,S_IRWXG,S_IRWXO
import sys
import time
import copy
import zlib
import shutil
import socket
import base64
import cPickle
import threading
import traceback
import matplotlib.cm as cm

sys.path.append("../")
try:
    import framework.constants as c
except ImportError:
    print "Please create and edit a constants.py from the template file provided"
    sys.exit(-1)

import framework.sanity_check
framework.sanity_check.all()


from framework.modules.modules import server_modules_dict
from framework.tools import helper_functions
from framework.tools.helper_functions import HeatmapOptions, SerializeToFile, DeserializeFromFile, GetCopy, RelativePath
from framework.tools.logger import debug

import framework.tools.rdp
import framework.tools.env
import framework.tools.qpcr
import framework.tools.vamps
import framework.tools.heatmap
import framework.tools.bar
import framework.tools.piechart
import framework.tools.diversityindex
import framework.tools.rarefaction
import framework.tools.taxons
import framework.tools.hcluster


def formatExceptionInfo(maxTBlevel=5):
    cla, exc, trbk = sys.exc_info()
    excName = cla.__name__
    try:
        excArgs = exc.__dict__["args"]
    except KeyError:
        excArgs = "<no args>"
    excTb = traceback.format_tb(trbk, maxTBlevel)
    text = ""
    text += excName + '\n'
    text += excArgs + '\n'
    for line in excTb:
        text += line
    return text


class ServerState:
    def __init__(self):
        self.running_analyses = []
        self.done_analyses = []
        self.refresh_analyses()

    def refresh_analyses(self):
        for dir in os.listdir(c.analyses_dir):
            if dir.startswith('.'):
                continue
            self.done_analyses.append(dir)


class Server:
    def __init__(self, socket_name):
        serversocket = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
        try:
            os.remove(c.socket_name)
        except:
            pass
        serversocket.bind(socket_name)
        os.chmod(socket_name,S_IRWXU|S_IRWXG|S_IRWXO)#set to 777 so apache can read/write
        serversocket.listen(5)

        serverstate = ServerState()

        print "\n* Server is up and running :)\n"

        last_thread = None

        while 1:
            try:
                (clientsocket, address) = serversocket.accept()
            except KeyboardInterrupt:
                print "interrupted.. closing socket"
                serversocket.close()
                os.remove(c.socket_name)
                sys.exit(0)

            threadid = str(time.time())
            thread = threading.Thread(target=ProcessRequest, args=(clientsocket,
                                                                   serverstate,
                                                                   threadid))
            thread.setName(threadid)
            thread.start()



class ProcessRequest:
    """
    takes a request through a UNIX domain socket `clientsocket`, and writes the 
server response to the socket. The socket should provide a python dict, 
for example the one passed into helper_functions.server. one of the functions 
in `executors` will be called based on `dict["request"]`



    """
    def __init__(self, clientsocket, serverstate, threadid):
        """
        reads one line of text from the clientsocket, passes the text through
        cPickle, then calls one of the functions in executors.
        """
        self.threadid = threadid#never used?
        self.clientsocket = clientsocket
        self.socket_is_alive = True
        self.serverstate = serverstate
        self.encode_response = lambda x: base64.encodestring(zlib.compress(cPickle.dumps(x), 9))
        self.decode_request  = lambda x: cPickle.loads(zlib.decompress(base64.decodestring(x)))
        self.request_dict = self.read_socket()

        print "\n\n* Incoming Data: ", self.request_dict

        executers = {'exec_analysis'                : self.exec_analysis,
                     'remove_analysis'              : self.remove_analysis,
                     'status'                       : self.status_request,
                     'get_analyses'                 : self.get_analyses,
                     'get_analysis_name'            : self.get_analysis_name,
                     'get_type_of_analysis'         : self.get_type_of_analysis,
                     'get_analysis_ranks'           : self.get_analysis_ranks,
                     'get_sample_map_name'          : self.get_sample_map_name,
                     'get_sample_maps'              : self.get_sample_maps,
                     'get_sample_map_instances'     : self.get_sample_map_instances,
                     'get_samples_dict_path'        : self.get_samples_dict_path,
                     'get_relative_taxon_charts_dir': self.get_relative_taxon_charts_dir,
                     'get_relative_type_specific_data_dir': self.get_relative_type_specific_data_dir,
                     'get_otu_confidence_tuples'    : self.get_otu_confidence_tuples,
                     'get_otu_t_p_tuples'           : self.get_otu_t_p_tuples,
                     'get_samples_in_an_analysis'   : self.get_samples_in_an_analysis,
                     'append_samples_to_analysis'   : self.append_samples_to_analysis,
                     'info'                         : self.get_analysis_info,
                     'refresh_analysis_files'       : self.refresh_analysis_files,
                     'heatmap_options'              : self.heatmap_options,
                     'refresh_heatmap'              : self.refresh_heatmap,
                     'refresh_sample_map'           : self.generate_or_refresh_sample_map,
                     'new_sample_map'               : self.generate_or_refresh_sample_map}


        if not executers.has_key(self.request_dict['request']):
            self.write_socket({'response': 'error', 'content': 'unknown request'})
            return
        elif not self.request_dict.has_key('time_stamp'):
            # time_stamp should be generated by "time" function in time module.
            self.write_socket({'response': 'error', 'content': 'request dict has to have a "time_stamp" variable'})
            return
        else:
            request_handler = executers.get(self.request_dict['request']).__name__
            time_stamp = self.request_dict['time_stamp']
            print "* Calling request handler: ", request_handler
            try:
                executers.get(self.request_dict['request'])()
            except:
                error_log = os.path.join(c.error_logs_dir, time_stamp.__str__())
                traceback.print_exc(file=open(error_log, "w"))
                if self.socket_is_alive:
                    exception_info = open(error_log).read()
                    self.write_socket({'response': 'error', 'time_stamp': time_stamp.__str__(), 'exception': exception_info})
                return

    def write_socket(self, response_dict):
        r = self.encode_response(response_dict)
        print "* Outgoing Data (%d bytes): " % len(r), response_dict
        total_sent = self.clientsocket.send(r)
        self.socket_is_alive = False
        return total_sent


    def read_socket(self):
        """
        loops over self.clientsocket in 512-byte chunks until a chunk ends with \n.
returns self.decode_request of the data recieved.
        """
        data = ""
        while True:
            chunk = self.clientsocket.recv(512)
            data += chunk
            if chunk[-1] == "\n":
                break
        return self.decode_request(data)

    def remove_analysis(self):
        analysis_id             = self.request_dict['analysis_id']

        #import pdb; pdb.set_trace()
        p = Meta(analysis_id)

        if analysis_id in self.serverstate.running_analyses:
            self.serverstate.running_analyses.remove(analysis_id)
        if analysis_id in self.serverstate.done_analyses:
            self.serverstate.done_analyses.remove(analysis_id)

        shutil.rmtree(p.dirs.analysis_dir)

        self.write_socket({'response': 'OK'})


    def exec_analysis(self):
        analysis_id             = self.request_dict['data_file_sha1sum']
        data_file_temp_path     = self.request_dict['data_file_path']
        job_description         = self.request_dict['job_description']
        analysis_type           = self.request_dict['analysis_type']

        late_response_request = self.request_dict.has_key('return_when_done') and self.request_dict['return_when_done'] == True
        #import pdb; pdb.set_trace()
        if analysis_type not in server_modules_dict:#this is where we could check filetype 
             self.write_socket({'response': 'error', 'content': 'Wrong type of analysis.'})
             return#fixes _framework.testServerError

        if(analysis_id in self.serverstate.running_analyses or
           analysis_id in self.serverstate.done_analyses):
            self.write_socket({'response':'error', 'content':'Analysis is already running'})
            return#fixes _framework.testRepeatAnalysis

        p = Meta(analysis_id)

        debug("Server state is being updated, running processes.APPEND(this)", p.files.log_file)
        self.serverstate.running_analyses.append(analysis_id)

        debug("Copying data file", p.files.log_file)
        shutil.copy(data_file_temp_path, os.path.join(p.dirs.analysis_dir, c.data_file_name))

        debug("Filling job description: '%s'" % job_description, p.files.log_file)
        open(p.files.job_file, 'w').write(job_description + '\n')

        if late_response_request is False:
            debug("Response is being sent", p.files.log_file)
            self.write_socket({'response': 'OK', 'process_id': analysis_id})

        ################################################################
        # call sever modules..
        ################################################################
        # analysis specific stuff.
        server_modules_dict[analysis_type]._exec(p, self.request_dict)

        # common analysis routines..
        server_modules_dict['commons']._exec(p, self.request_dict)
        ################################################################

        # update server state so the info page is browsable.
        debug("Server state is being updated, running analyses.REMOVE(this), done analyses.APPEND(this)", p.files.log_file)
        self.serverstate.running_analyses.remove(analysis_id)
        self.serverstate.done_analyses.append(analysis_id)
        debug("Info page is ready for this study.", p.files.log_file)

        if late_response_request is True:
            debug("Response is being sent", p.files.log_file)
            self.write_socket({'response': 'OK', 'process_id': analysis_id})

    def get_samples_dict_path(self):
        analysis_id = self.request_dict['analysis_id']

        p = Meta(analysis_id)

        self.write_socket({'response': 'OK', 'samples_dict_path': p.files.samples_serialized_file_path})

    def refresh_heatmap(self):
        analysis_id = self.request_dict['analysis_id']
        instance    = self.request_dict['instance']
        options     = self.request_dict['options']
        rank        = self.request_dict['rank']

        p = Meta(analysis_id)

        p.dirs.change_current_sample_map_instance(p.files, instance)

        options.abundance_file = RelativePath(vars(p.files)[c.percent_abundance_file_prefix + rank + '_file_path'])
        options.output_file = RelativePath(vars(p.files)[c.abundance_heatmap_file_prefix + rank + '_file_path'])
        SerializeToFile(options, vars(p.files)[c.heatmap_options_file_prefix + rank + '_file_path'])
        try:
            framework.tools.heatmap.main(options, c.analyses_dir)
        except:
            self.write_socket({'response': 'error', 'content': formatExceptionInfo()})
            return

        self.write_socket({'response': 'OK', 'options': options})


    def heatmap_options(self):
        analysis_id = self.request_dict['analysis_id']
        instance    = self.request_dict['instance']
        rank        = self.request_dict['rank']

        p = Meta(analysis_id)

        p.dirs.change_current_sample_map_instance(p.files, instance)

        self.write_socket({'response': 'OK', 'options': DeserializeFromFile(vars(p.files)[c.heatmap_options_file_prefix + rank + '_file_path'])})


    def generate_or_refresh_sample_map(self):
        analysis_id = self.request_dict['analysis_id']

        p = Meta(analysis_id)

        # update server state
        debug("Server state is being updated, running analyses.APPEND(this)", p.files.log_file)
        self.serverstate.done_analyses.remove(analysis_id)
        self.serverstate.running_analyses.append(analysis_id)

        # read the original sampels dict and otu library
        samples_dict = DeserializeFromFile(p.files.samples_serialized_file_path)
        otu_library  = DeserializeFromFile(p.files.otu_library_file_path)

        # if request dict has 'instance', sample map exists and needs to be refreshed
        if self.request_dict.has_key('instance'):
            instance = self.request_dict['instance']

            # if late response wasn't requested send response immediately
            if not self.request_dict.has_key('return_when_done'):
                self.write_socket({'response': 'OK'})

            p.dirs.change_current_sample_map_instance(p.files, instance)

            filtered_samples_dict = DeserializeFromFile(p.files.sample_map_filtered_samples_dict_file_path)

        # else, this is a new sample map request.
        else:
            sample_map_name = self.request_dict['sample_map_dict']['sample_map_name']
            sample_map_list = self.request_dict['sample_map_dict']['sample_map_list']

            self.write_socket({'response': 'OK'})

            # get a new instance id for the analysis and create sample map directories
            debug("Creating new sample map directory for '%s'" % sample_map_name, p.files.log_file)
            p.dirs.create_new_sample_map_instance(p.files)
            debug("Current sample map directory is '%s'" % p.dirs.sample_map_instance_dir, p.files.log_file)

            # store sample map name
            open(p.files.sample_map_name_file_path, 'w').write(sample_map_name + '\n')
            debug("Sample map name has been stored", p.files.log_file)

            # store sample map
            f = open(p.files.sample_map_file_path, 'w')
            for sample in sample_map_list:
                f.write('%(sample)s\t%(group)s\t%(color)s\n' % sample)
            f.close()
            debug("Sample map has been stored", p.files.log_file)

            # get filtered samples dict and store it for sample map
            debug("Filtered samples dict are being generated and stored", p.files.log_file)
            filtered_samples_dict = framework.tools.helper_functions.filter_dict(samples_dict, keep_only = [s['sample'] for s in sample_map_list])
            SerializeToFile(filtered_samples_dict, p.files.sample_map_filtered_samples_dict_file_path)


        sample_map_functions_common_dict = server_modules_dict['commons']._sample_map_functions(p, self.request_dict)
        common_function_ids = sample_map_functions_common_dict.keys()
        common_function_ids.sort()
        for id in common_function_ids:
            sample_map_functions_common_dict[id]['func'](p)

        sample_map_functions_module_dict = server_modules_dict[p.type]._sample_map_functions(p, self.request_dict)
        module_function_ids = sample_map_functions_module_dict.keys()
        module_function_ids.sort()
        for id in module_function_ids:
            sample_map_functions_module_dict[id]['func'](p)


        # update server state
        debug("Server state is being updated, running analyses.REMOVE(this), done analyses.APPEND(this)", p.files.log_file)
        self.serverstate.running_analyses.remove(analysis_id)
        self.serverstate.done_analyses.append(analysis_id)

        debug("All files for sample map has been generated", p.files.log_file)

        # if late response was requested, send it now
        if self.request_dict.has_key('return_when_done'):
            self.write_socket({'response': 'OK'})


    def get_analyses(self):
        analyses = []
        """returns analyses that are running on the server or were finished"""
        for analysis_id in self.serverstate.running_analyses:
            p = Meta(analysis_id)
            name = open(p.files.job_file).read().strip()
            analyses.append({'id': analysis_id,
                             'name': name,
                             'type': p.type,
                             'state': 'running',
                             'log': open(p.files.log_file).readlines()[-5:]})

        for analysis_id in self.serverstate.done_analyses:
            p = Meta(analysis_id)
            name = open(p.files.job_file).read().strip()
            analyses.append({'id': analysis_id,
                             'name': name,
                             'type': p.type,
                             'state': 'done',
                             'log': open(p.files.log_file).readlines()[-5:]})

        #import pdb; pdb.set_trace()
        self.write_socket({'response': 'OK', 'analyses': analyses})


    def get_sample_map_name(self):
        analysis_id = self.request_dict['analysis_id']
        instance = self.request_dict['instance']

        p = Meta(analysis_id)

        p.dirs.change_current_sample_map_instance(p.files, instance)

        self.write_socket({'response': 'OK', 'name': open(p.files.sample_map_name_file_path).read().strip()})


    def get_analysis_ranks(self):
        analysis_id = self.request_dict['analysis_id']

        p = Meta(analysis_id)

        self.write_socket({'response': 'OK', 'analysis_ranks': c.ranks[p.type]})


    def get_analysis_name(self):
        analysis_id = self.request_dict['analysis_id']

        p = Meta(analysis_id)

        self.write_socket({'response': 'OK', 'name': open(p.files.job_file).read().strip()})


    def get_type_of_analysis(self):
        analysis_id = self.request_dict['analysis_id']

        p = Meta(analysis_id)

        self.write_socket({'response': 'OK', 'type_of_analysis': p.type})

    def append_samples_to_analysis(self):
        analysis_id         = self.request_dict['analysis_id']
        data_file_temp_path = self.request_dict['data_file_path']
        self.serverstate.done_analyses.remove(analysis_id)
        self.serverstate.running_analyses.append(analysis_id)

        p = Meta(analysis_id)

        additional_data_file_path = os.path.join(p.dirs.analysis_dir, "additional_data_file")
        debug("Copying additional data file", p.files.log_file)
        shutil.copy(data_file_temp_path, additional_data_file_path)

        self.request_dict['additional_data_file_path'] = additional_data_file_path

        if not self.request_dict.get('return_when_done'):
            self.write_socket({'response': 'OK'})

        ################################################################
        # call server modules for append..
        ################################################################
        # analysis specific stuff.
        server_modules_dict[p.type]._append(p, self.request_dict)

        # common analysis routines..
        server_modules_dict['commons']._append(p, self.request_dict)
        ################################################################

        os.remove(additional_data_file_path)
        self.serverstate.running_analyses.remove(analysis_id)
        self.serverstate.done_analyses.append(analysis_id)
        debug("Done.", p.files.log_file)

        if self.request_dict.get('return_when_done'):
            self.write_socket({'response': 'OK'})

    def refresh_analysis_files(self):
        analysis_id = self.request_dict['analysis_id']

        p = Meta(analysis_id)

        functions_module_dict = server_modules_dict[p.type]._module_functions(p, self.request_dict)
        functions_common_dict = server_modules_dict['commons']._module_functions(p, self.request_dict)

        if self.request_dict.has_key('get_refresh_options'):
            refresh_options_module = functions_module_dict.keys()
            refresh_options_common = functions_common_dict.keys()

            refresh_options_module.sort()
            refresh_options_common.sort()

            refresh_options = refresh_options_module + refresh_options_common

            print refresh_options

            functions_dict = {}
            functions_dict.update(functions_module_dict)
            functions_dict.update(functions_common_dict)

            # this is important. functions_dict contains function names,
            # descriptions, as well as actual memory references to functions
            # exported by protocol specific and common module provide.
            #
            # memory references are meaningful in the context of the server
            # and they shouldn't be sent to clients (since clients can not
            # do anything with them).
            #
            # here, I am solving the problem by stripping those references
            # from the data structure with my dirty loop before writing sending
            # response data back to the client. a better solution could replace
            # this anytime.
            for module_item in functions_dict:
                functions_dict[module_item]['func'] = None

            self.write_socket({'response': 'OK', 'refresh_options': refresh_options, 'functions_dict': functions_dict})
        else:
            refresh_requests = self.request_dict['refresh_requests']

            # if late response wasn't requested send response immediately
            if not self.request_dict.has_key('return_when_done'):
                self.write_socket({'response': 'OK'})

            # trixy part:
            for request in refresh_requests:
                if request in functions_module_dict:
                    functions_module_dict[request]['func'](p)
                elif request in functions_common_dict:
                    functions_common_dict[request]['func'](p)

            # send the late response if it was requested
            if self.request_dict.has_key('return_when_done'):
                self.write_socket({'response': 'OK'})

        debug("Done with refresh tasks.", p.files.log_file)


    def get_sample_map_instances(self):
        analysis_id = self.request_dict['analysis_id']

        p = Meta(analysis_id)

        instances = framework.tools.helper_functions.sorted_copy(p.dirs.get_sample_map_instances())

        meta = {}

        for instance in instances:
            p.dirs.change_current_sample_map_instance(p.files, instance)
            name = open(p.files.sample_map_name_file_path).read().strip()
            sample_groups, group_colors = helper_functions.get_groups_colors_from_sample_map_file(p.files.sample_map_file_path)
            meta[instance] = {'name': name or "Noname",
                              'sample_groups': sample_groups,
                              'group_colors': group_colors}

        self.write_socket({'response': 'OK', 'instances': instances, 'meta': meta })

    def get_otu_confidence_tuples(self):
        analysis_id = self.request_dict['analysis_id']
        rank =  self.request_dict['rank']

        p = Meta(analysis_id)

        otu_confidence_tuples = DeserializeFromFile(os.path.join(p.dirs.type_specific_data_dir, rank + '_rdp_confidence_ordering_info'))

        self.write_socket({'response': 'OK', 'otu_confidence_tuples': otu_confidence_tuples})

    def get_relative_type_specific_data_dir(self):
        analysis_id = self.request_dict['analysis_id']

        p = Meta(analysis_id)

        relative_type_specific_data_dir = RelativePath(p.dirs.type_specific_data_dir)

        self.write_socket({'response': 'OK', 'relative_type_specific_data_dir': relative_type_specific_data_dir})

    def get_relative_taxon_charts_dir(self):
        analysis_id = self.request_dict['analysis_id']
        instance    = self.request_dict['instance']

        p = Meta(analysis_id)

        p.dirs.change_current_sample_map_instance(p.files, instance)

        relative_taxon_charts_dir = RelativePath(p.dirs.sample_map_taxon_charts_dir)

        self.write_socket({'response': 'OK', 'taxon_charts_dir': relative_taxon_charts_dir})


    def get_otu_t_p_tuples(self):
        analysis_id = self.request_dict['analysis_id']
        instance    = self.request_dict['instance']
        if self.request_dict.has_key('rank'):
            rank        = self.request_dict['rank']
        else:
            rank = None

        p = Meta(analysis_id)

        p.dirs.change_current_sample_map_instance(p.files, instance)

        sample_groups, group_colors = helper_functions.get_groups_colors_from_sample_map_file(p.files.sample_map_file_path)

        otu_t_p_tuple_dict = DeserializeFromFile(p.files.sample_map_otu_t_p_tuples_dict_file_path)

        if rank:
            self.write_socket({'response': 'OK', 'otu_t_p_tuple_list': otu_t_p_tuple_dict[rank] })
        else:
            self.write_socket({'response': 'OK', 'otu_t_p_tuple_dict': otu_t_p_tuple_dict })


    def get_sample_maps(self):
        analysis_id = self.request_dict['analysis_id']

        p = Meta(analysis_id)

        maps = []

        # if instance specified, return only that, otherwise return all sample maps.
        sample_map_instances = []
        if self.request_dict.has_key('instance'):
            sample_map_instances.append(self.request_dict['instance'])
        else:
            sample_map_instances = p.dirs.get_sample_map_instances()

        for instance in sample_map_instances:
            p.dirs.change_current_sample_map_instance(p.files, instance)
            maps.append(helper_functions.get_sample_map_dict(p))

        self.write_socket({'response': 'OK', 'sample_maps': maps})


    def get_analysis_info(self):
        analysis_id = self.request_dict['analysis_id']

        p = Meta(analysis_id)

        info_dict = {'id': analysis_id,
                     'name': open(p.files.job_file).read().strip(),
                     'type': p.type,
                     'ranks': c.ranks[p.type],
                     'rdp_output_file_exists': os.path.exists(p.files.rdp_output_file_path),
                     'rdp_output_file_path'  : os.path.join(analysis_id, c.rdp_output_file_name),
                     'all_unique_samples_list': framework.tools.helper_functions.sorted_copy([sample.strip() for sample in open(p.files.all_unique_samples_file_path).readlines()]),
                     'samples_sequences_bar': os.path.join(analysis_id, c.samples_sequences_bar_name),
                     'pie_charts_dir' : os.path.join(analysis_id, c.pie_charts_dir_name),
                     'rarefaction_all_samples_exists': os.path.exists(p.files.rarefaction_curves_all_samples_file_path),
                     'rarefaction_all_samples': os.path.join(analysis_id, c.rarefaction_curves_all_samples_file_name),
                     'rarefaction_curves_dir': os.path.join(analysis_id, c.rarefaction_curves_dir_name),
                     'rarefaction_prefix': c.rarefaction_curve_file_prefix,
                     'rarefaction_postfix': c.rarefaction_curve_file_postfix,
                     'shannon_diversity_index_img': os.path.join(analysis_id, c.shannon_diversity_index_img_name),
                     'simpsons_diversity_index_img': os.path.join(analysis_id, c.simpsons_diversity_index_img_name),
                     'shannon_diversity_index_data': os.path.join(analysis_id, c.shannon_diversity_index_data_name),
                     'simpsons_diversity_index_data': os.path.join(analysis_id, c.simpsons_diversity_index_data_name)}

        self.write_socket({'response': 'OK', 'info': info_dict})


    def get_samples_in_an_analysis(self):
        analysis_id = self.request_dict['analysis_id']

        p = Meta(analysis_id)

        samples = framework.tools.helper_functions.sorted_copy([sample.strip() for sample in open(p.files.all_unique_samples_file_path).readlines()])

        self.write_socket({'response': 'OK', 'samples': samples})


    def status_request(self):
        self.write_socket({'response': 'OK', 'running_analyses': self.serverstate.running_analyses, 'done_analyses': self.serverstate.done_analyses})


class Dirs:
    def __init__(self, analysis_id):
        self.analysis_dir = os.path.join(c.analyses_dir, analysis_id)
        self.sample_map_instance = None
        self.sample_map_instance_dir = None
        self.sample_map_taxon_charts_dir = None
        self.sample_map_heatmaps_dir = None
        self.sample_map_dendrograms_dir = None

        if not os.path.exists(self.analysis_dir):
            os.makedirs(self.analysis_dir)

        self.sample_maps_dir = os.path.join(self.analysis_dir, c.sample_maps_dir_name)
        if not os.path.exists(self.sample_maps_dir):
            os.makedirs(self.sample_maps_dir)

        self.pie_charts_dir = os.path.join(self.analysis_dir, c.pie_charts_dir_name)
        if not os.path.exists(self.pie_charts_dir):
            os.makedirs(self.pie_charts_dir)

        self.rarefaction_curves_dir = os.path.join(self.analysis_dir, c.rarefaction_curves_dir_name)
        if not os.path.exists(self.rarefaction_curves_dir):
            os.makedirs(self.rarefaction_curves_dir)

        self.type_specific_data_dir = os.path.join(self.analysis_dir, c.type_specific_figures_dir_name)
        if not os.path.exists(self.type_specific_data_dir):
            os.makedirs(self.type_specific_data_dir)

    def get_sample_map_instances(self):
        return [dir for dir in os.listdir(self.sample_maps_dir) if not dir.startswith('.')]

    def create_new_sample_map_instance(self, files):
        next_available_sample_map_dir = len(self.get_sample_map_instances()) + 1
        
        # make it sure that the assumption of next_available_sample_map_dir
        # holds true even if some of the sample maps were deleted:
        while os.path.exists(os.path.join(self.sample_maps_dir, str(next_available_sample_map_dir))):
            next_available_sample_map_dir += 1

        self.sample_map_instance_dir = os.path.join(self.sample_maps_dir, str(next_available_sample_map_dir))
        os.makedirs(self.sample_map_instance_dir)
        self.sample_map_taxon_charts_dir = os.path.join(self.sample_map_instance_dir, c.sample_map_taxon_charts_dir_name)
        os.makedirs(self.sample_map_taxon_charts_dir)
        self.sample_map_heatmaps_dir = os.path.join(self.sample_map_instance_dir, c.sample_map_heatmaps_dir_name)
        os.makedirs(self.sample_map_heatmaps_dir)
        self.sample_map_dendrograms_dir = os.path.join(self.sample_map_instance_dir, c.sample_map_dendrograms_dir_name)
        os.makedirs(self.sample_map_dendrograms_dir)
        files.update_sample_map_files_info()

    def change_current_sample_map_instance(self, files, instance):
        self.sample_map_instance = instance
        self.sample_map_instance_dir = os.path.join(self.sample_maps_dir, str(instance))
        self.sample_map_taxon_charts_dir = os.path.join(self.sample_map_instance_dir, c.sample_map_taxon_charts_dir_name)
        self.sample_map_heatmaps_dir = os.path.join(self.sample_map_instance_dir, c.sample_map_heatmaps_dir_name)
        self.sample_map_dendrograms_dir = os.path.join(self.sample_map_instance_dir, c.sample_map_dendrograms_dir_name)

        #make sure these directories exist:
        if not os.path.exists(self.sample_map_taxon_charts_dir):
            os.makedirs(self.sample_map_taxon_charts_dir)
        if not os.path.exists(self.sample_map_heatmaps_dir):
            os.makedirs(self.sample_map_heatmaps_dir)
        if not os.path.exists(self.sample_map_dendrograms_dir):
            os.makedirs(self.sample_map_dendrograms_dir)

        files.update_sample_map_files_info()


class Images:
    def __init__(self, dirs):
        self.samples_sequences_bar_path         = os.path.join(dirs.analysis_dir, c.samples_sequences_bar_name)
        self.simpsons_diversity_index_img_path  = os.path.join(dirs.analysis_dir, c.simpsons_diversity_index_img_name)
        self.shannon_diversity_index_img_path   = os.path.join(dirs.analysis_dir, c.shannon_diversity_index_img_name)

class Files:
    def __init__(self, dirs):
        self.dirs                         = dirs

        J = lambda x: os.path.join(self.dirs.analysis_dir, x)

        self.data_file_path                        = J(c.data_file_name)
        self.rdp_output_file_path                  = J(c.rdp_output_file_name)
        self.all_unique_samples_file_path          = J(c.all_unique_samples_file_name)
        self.otu_library_file_path                 = J(c.otu_library_file_name)
        self.rdp_error_log_file_path               = J(c.rdp_error_log_file_name)
        self.seperator_file_path                   = J(c.seperator_file_name)
        self.log_file                              = J(c.log_file_name)
        self.job_file                              = J(c.job_name_file_name)
        self.type_of_analysis_file_path            = J(c.type_of_analysis_file_name)
        self.samples_serialized_file_path          = J(c.samples_serialized_file_name)
        self.rarefaction_dict_serialized_file_path = J(c.rarefaction_dict_serialized_file_name)
        self.rarefaction_curves_all_samples_file_path = J(c.rarefaction_curves_all_samples_file_name)
        self.simpsons_diversity_index_data_path  = os.path.join(dirs.analysis_dir, c.simpsons_diversity_index_data_name)
        self.shannon_diversity_index_data_path   = os.path.join(dirs.analysis_dir, c.shannon_diversity_index_data_name)

        self.sample_map_name_file_path                     = None
        self.sample_map_file_path                          = None
        self.sample_map_otu_t_p_tuples_dict_file_path      = None
        self.sample_map_otu_t_p_tuples_dict_real_file_path = None
        self.sample_map_filtered_samples_dict_file_path    = None

        self.taxa_color_dict_file_path         = J(c.taxa_color_dict_file_name)

    def update_sample_map_files_info(self):
        J = lambda x: os.path.join(self.dirs.sample_map_instance_dir, x)
        H = lambda x: os.path.join(self.dirs.sample_map_instance_dir, c.sample_map_heatmaps_dir_name, x)

        self.sample_map_name_file_path                     = J(c.sample_map_name_file_name)
        self.sample_map_file_path                          = J(c.sample_map_file_name)
        self.sample_map_otu_t_p_tuples_dict_file_path      = J(c.sample_map_otu_t_p_tuples_dict_file_name)
        self.sample_map_otu_t_p_tuples_dict_real_file_path = J(c.sample_map_otu_t_p_tuples_dict_real_file_name)
        self.sample_map_filtered_samples_dict_file_path    = J(c.sample_map_filtered_samples_dict_file_name)

        for levels_list in c.ranks.values():
            for level in levels_list:
                prefix = c.percent_abundance_file_prefix
                vars(self)['%s%s_file_path' % (prefix, level)] = J('%s%s' % (prefix, level))
                prefix = c.abundance_heatmap_file_prefix
                vars(self)['%s%s_file_path' % (prefix, level)] = H('%s%s.png' % (prefix, level))
                prefix = c.heatmap_options_file_prefix
                vars(self)['%s%s_file_path' % (prefix, level)] = H('%s%s' % (prefix, level))


class Meta:
    """
    Meta-info for a particular analysis. contains - 
dirs - Dirs object
files - Files object
images - Images object
type - str
desc - str
    """
    def __init__(self, analysis_id):
        self.dirs = Dirs(analysis_id)
        self.files = Files(self.dirs)
        self.images = Images(self.dirs)
        self.type = self.get_analysis_type()
        self.desc = self.get_analysis_desc()

    def set_analysis_type(self, type):
        if type in c.ranks.keys():
            self.type = type
            open(self.files.type_of_analysis_file_path, 'w').write(type)

    def get_analysis_type(self):
        if os.path.exists(self.files.type_of_analysis_file_path):
            return open(self.files.type_of_analysis_file_path).read().strip()
        else:
            return None

    def get_analysis_desc(self):
        if os.path.exists(self.files.job_file):
            return open(self.files.job_file).read().strip()
        else:
            return None

if __name__ == '__main__':
    """Initializes the Server with the socket specified in config.py"""
    Server(c.socket_name)
