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
# Web client core. Talks to the server, generates web pages for analyses.
#


import os
import sys
import base64
import socket
import cPickle
import zlib

from django.http import HttpResponse
from django.template.loader import get_template
from django.template import Context

sys.path.append("../..")
sys.path.append("../../..")
from framework import constants

from framework import helper_functions
from framework.tools.logger import debug
from framework.clients.ferrisweb import webforms

server = helper_functions.server

def server_err(server_dict):
    if server_dict.has_key('response'):
        return server_dict['response'] == 'error'
    else:
        return True

def err_response(server_dict):
    context_dict = {}

    if server_dict.has_key('content'):
        context_dict['content'] =  server_dict['content']
    if server_dict.has_key('exception'):
        context_dict['exception'] =  server_dict['exception']
    if server_dict.has_key('time_stamp'):
        context_dict['time_stamp'] = server_dict['time_stamp']
    if not len(server_dict):
        context_dict['content'] =  "Either server is not running or socket name is wrong"

    return HttpResponse(get_template("error.tmpl").render(Context(context_dict)))


def sample_map_instances(request, analysis_id):
    server_request = {'request': 'get_sample_map_instances', 'analysis_id': analysis_id}
    server_response = server(server_request)
    sample_map_instances = server_response['sample_map_instances']

    return HttpResponse(get_template("simple.tmpl").render(Context({'content': "Analysis has %d sample maps: %s" % (len(sample_map_instances), sample_map_instances.__str__())})))

def sample_map_instance(request, analysis_id, instance):
    server_request = {'request': 'get_sample_maps', 'instance': instance, 'analysis_id': analysis_id}
    server_response = server(server_request)
    sample_maps = server_response['sample_maps']

    server_request = {'request': 'get_analysis_name', 'analysis_id': analysis_id}
    server_response = server(server_request)
    analysis_name = server_response['name']

    server_request = {'request': 'info', 'analysis_id': analysis_id}
    server_response = server(server_request)
    analysis_info = server_response['info']

    server_request = {'request': 'get_otu_t_p_tuples', 'analysis_id': analysis_id, 'instance': instance}
    server_response = server(server_request)
    otu_t_p_tuple_dict = server_response['otu_t_p_tuple_dict']

    samples_genus_OTUs = get_samples_genus_OTUs(analysis_id)

    return HttpResponse(get_template("sample_map.tmpl").render(Context({'map': sample_maps[0],
                                                                        'analysis_info': analysis_info,
                                                                        'otu_t_p_tuple_dict': otu_t_p_tuple_dict,
                                                                        'samples_genus_OTUs': samples_genus_OTUs,
                                                                        'analysis_id': analysis_id})))

def sample_map_dot(request, analysis_id, instance, rank, real_abundance = False):
    server_request = {'request': 'get_otu_t_p_tuples', 'analysis_id': analysis_id, 'instance': instance, 'rank': rank}
    server_response = server(server_request)
    otu_t_p_tuple_list = server_response['otu_t_p_tuple_list']

    server_request = {'request': 'get_analysis_name', 'analysis_id': analysis_id}
    server_response = server(server_request)
    analysis_name = server_response['name']

    server_request = {'request': 'get_sample_map_name', 'analysis_id': analysis_id, 'instance': instance}
    server_response = server(server_request)
    sample_map_name = server_response['name']

    server_request = {'request': 'get_analysis_ranks', 'analysis_id': analysis_id}
    server_response = server(server_request)
    analysis_ranks = server_response['analysis_ranks']

    server_request = {'request': 'get_relative_taxon_charts_dir', 'analysis_id': analysis_id, 'instance': instance}
    server_response = server(server_request)
    taxon_charts_dir = server_response['taxon_charts_dir']

    if real_abundance:
        tmpl = get_template("sample_map_dot_real.tmpl")
    else:
        tmpl = get_template("sample_map_dot.tmpl")

    return HttpResponse(tmpl.render(Context({'otu_t_p_tuple_list': otu_t_p_tuple_list,
                                             'instance': instance,
                                             'analysis_name': analysis_name,
                                             'taxon_charts_dir': taxon_charts_dir,
                                             'sample_map_name': sample_map_name,
                                             'rank': rank,
                                             'ranks': analysis_ranks,
                                             'analysis_id': analysis_id})))

def dendrogram_detail(request, analysis_id, instance, rank):
    server_request = {'request': 'get_sample_maps', 'instance': instance, 'analysis_id': analysis_id}
    server_response = server(server_request)
    sample_maps = server_response['sample_maps']

    server_request = {'request': 'get_analysis_name', 'analysis_id': analysis_id}
    server_response = server(server_request)
    analysis_name = server_response['name']

    server_request = {'request': 'get_analysis_ranks', 'analysis_id': analysis_id}
    server_response = server(server_request)
    analysis_ranks = server_response['analysis_ranks']


    return HttpResponse(get_template("sample_map_dendrogram.tmpl").render(Context({'map': sample_maps[0],
                                                                        'analysis_name': analysis_name,
                                                                        'instance': instance,
                                                                        'rank': rank,
                                                                        'ranks': analysis_ranks,
                                                                        'analysis_id': analysis_id})))

def heatmap_detail(request, analysis_id, instance, rank):
    server_request = {'request': 'get_analysis_name', 'analysis_id': analysis_id}
    server_response = server(server_request)
    analysis_name = server_response['name']

    server_request = {'request': 'get_sample_maps', 'analysis_id': analysis_id}
    server_response = server(server_request)
    sample_maps = server_response['sample_maps']

    image = None
    for map in sample_maps:
        if map['instance'] == instance:
            for r, i in map['heatmaps'].items():
                if r == rank:
                    image = i

    server_request = {'request': 'get_sample_map_name', 'analysis_id': analysis_id, 'instance': instance}
    server_response = server(server_request)
    sample_map_name = server_response['name']

    server_request = {'request': 'heatmap_options', 'analysis_id': analysis_id, 'instance': instance, 'rank': rank}
    options = server(server_request)['options']

    if request.method == 'POST':
        width, height = 0, 0
        if request.POST['width'].strip() != '':
            width = int(request.POST['width'])
        if request.POST['height'].strip() != '':
            height = int(request.POST['height'])

        options.min_percentage = float(request.POST['min_percentage'])
        options.min_present = int(request.POST['min_present'])
        options.log = request.POST['log'] == 'True'
        options.width = width
        options.height = height
        options.margin_right = float(request.POST['margin_right'])
        options.margin_bottom = float(request.POST['margin_bottom'])
        options.cexRow = float(request.POST['cexRow'])
        options.cexCol = float(request.POST['cexCol'])

        server_request = {'request': 'refresh_heatmap', 'analysis_id': analysis_id, 'instance': instance, 'rank': rank, 'options': options, 'sample_map_name': sample_map_name}
        server_response = server(server_request)

        if server_err(server_response):
            return err_response(server_response)

        options = server_response['options']

    else:
        pass


    return HttpResponse(get_template("heatmap_detail.tmpl").render(Context({'options': options,
                                                                            'analysis_name': analysis_name,
                                                                            'analysis_id': analysis_id,
                                                                            'image': image,
                                                                            'rank': rank,
                                                                            'sample_map_name': sample_map_name,
                                                                            'instance': instance})))

def create_sample_map(request, analysis_id, step):
    Encode = lambda x: base64.encodestring(cPickle.dumps(x))
    Decode = lambda x: cPickle.loads(base64.decodestring(x))

    def get_sample_names():
        server_request = {'request': 'get_samples_in_an_analysis', 'analysis_id': analysis_id}
        server_response = server(server_request)
        return server_response['samples']

    def get_analysis_name():
        server_request = {'request': 'get_analysis_name', 'analysis_id': analysis_id}
        server_response = server(server_request)
        return server_response['name']

    analysis_name = get_analysis_name()

    step = int(step)

    if request.method == 'POST' and step == 1:
        sample_map_dict = {}
        sample_map_dict['sample_map_name'] = request.POST['sample_map_name']
        sample_map_dict['sample_map_list'] = []

        for sample in get_sample_names():
            if request.POST[sample]:
                sample_map_dict['sample_map_list'].append({'sample': sample, 'group': request.POST[sample].strip()})

        groups = list(set([x['group'] for x in sample_map_dict['sample_map_list']]))

        return HttpResponse(get_template("sample_map_form_1.tmpl").render(Context({'values_obj': Encode(sample_map_dict),
                                                                                   'sample_map_name': sample_map_dict['sample_map_name'],
                                                                                   'analysis_id': analysis_id,
                                                                                   'analysis_name': analysis_name,
                                                                                   'step': step,
                                                                                   'next_step': step + 1,
                                                                                   'groups': groups})))

    elif request.method == 'POST' and step == 2:
        sample_map_dict = Decode(request.POST['values_obj'])
        for m in sample_map_dict['sample_map_list']:
            m['color'] = request.POST[m['group']]

        return HttpResponse(get_template("sample_map_form_2.tmpl").render(Context({'values_obj': Encode(sample_map_dict),
                                                                                   'sample_map_dict': sample_map_dict,
                                                                                   'analysis_id': analysis_id,
                                                                                   'analysis_name': analysis_name,
                                                                                   'step': step,
                                                                                   'next_step': step + 1})))

    elif request.method == 'POST' and step == 3:
        sample_map_dict = Decode(request.POST['values_obj'])

        server_request = {'request': 'new_sample_map', 'analysis_id': analysis_id, 'sample_map_dict': sample_map_dict}
        #sample_map_dict = {'sample_map_name': u'name', 'sample_map_list': [{'sample': 'MZH-92', 'color': u'#87CEEB', 'group': u'456'} (...)]}
        server_response = server(server_request)

        if server_response['response'] == 'OK':
            tmpl = get_template("simple.tmpl")
            return HttpResponse(tmpl.render(Context({'content': "Your sample map submitted to server queue"})))


    else:
        step = 0
        server_request = {'request': 'status'}
        server_response = server(server_request)
        if not server_response:
            return HttpResponse("error when connecting to server: either server is not running or socket name is wrong")
        if analysis_id not in server_response['running_analyses'] + server_response['done_analyses']:
            return HttpResponse("wrong analysis id, server doesn't have anything like this")

        samples = get_sample_names()

        return HttpResponse(get_template("sample_map_form.tmpl").render(Context({'samples': samples,
                                                                                 'analysis_name': analysis_name,
                                                                                 'analysis_id': analysis_id,
                                                                                 'step': step,
                                                                                 'next_step': step + 1})))

def refresh_sample_map(request, analysis_id, instance):
    server_request = {'request': 'refresh_sample_map', 'analysis_id': analysis_id, 'instance': instance}
    server_response = server(server_request)

    return HttpResponse(get_template("simple.tmpl").render(Context({'content': server_response})))

def refresh_analysis_files(request, analysis_id):
    server_request = {'request': 'refresh_analysis_files', 'analysis_id': analysis_id, 'get_refresh_options': 1}
    server_response = server(server_request)

    refresh_options = server_response['refresh_options']
    functions_dict = server_response['functions_dict']

    if request.method == 'POST':
        refresh_requests = []
        for opt in refresh_options:
            if opt in request.POST.keys():
                refresh_requests.append(opt)
        if len(refresh_requests):
            server_request = {'request': 'refresh_analysis_files', 'analysis_id': analysis_id, 'refresh_requests': refresh_requests}
            server_response = server(server_request)

            return HttpResponse(get_template("simple.tmpl").render(Context({'content': "%d refresh requests has been submitted." % len(refresh_requests)})))
        else:
            return HttpResponse(get_template("simple.tmpl").render(Context({'content': "You haven't selected anything and that's perfectly OK."})))
    else:
        return HttpResponse(get_template("refresh.tmpl").render(Context({'refresh_options': refresh_options,
                                                                         'functions_dict': functions_dict,
                                                                         'analysis_id': analysis_id})))


def index(request):
    server_request = {'request': 'get_analyses'}
    server_response = server(server_request)

    if server_err(server_response):
        return err_response(server_response)

    analyses = server_response['analyses']
    return HttpResponse(get_template("index.tmpl").render(Context({'analyses': analyses})))


def get_samples_genus_OTUs(analysis_id):
    server_request = {'request': 'get_samples_dict_path', 'analysis_id': analysis_id}
    server_response = server(server_request)
    samples_dict_path = server_response['samples_dict_path']

    server_request = {'request': 'get_type_of_analysis', 'analysis_id': analysis_id}
    server_response = server(server_request)
    type_of_analysis = server_response['type_of_analysis']

    samples_dict = cPickle.load(open(samples_dict_path))

    Sort = lambda x: sorted(x.iteritems(), key=lambda (k,v):(v,k), reverse=True)
    samples_genus_OTUs = {}
    for sample in samples_dict:
        if type_of_analysis == "rdp":
            samples_genus_OTUs[sample] = Sort(samples_dict[sample]['genus'])
        else:
            samples_genus_OTUs[sample] = Sort(samples_dict[sample]['species'])


    return samples_genus_OTUs

def confidence_per_otu(request, analysis_id):
    rank = "genus"

    server_request = {'request': 'get_analysis_name', 'analysis_id': analysis_id}
    server_response = server(server_request)
    analysis_name = server_response['name']

    server_request = {'request': 'get_otu_confidence_tuples', 'analysis_id': analysis_id, 'rank': rank}
    server_response = server(server_request)
    otu_confidence_tuples = server_response['otu_confidence_tuples']

    server_request = {'request': 'get_relative_type_specific_data_dir', 'analysis_id': analysis_id}
    server_response = server(server_request)
    relative_type_specific_data_dir = server_response['relative_type_specific_data_dir']

    return HttpResponse(get_template("confidence_per_otu.tmpl").render(Context({'analysis_name': analysis_name,
                                                                                'analysis_id': analysis_id,
                                                                                'rank': rank,
                                                                                'relative_type_specific_data_dir': relative_type_specific_data_dir,
                                                                                'otu_confidence_tuples': otu_confidence_tuples})))

def analysis_dendrograms(request, analysis_id):
    server_request = {'request': 'get_analysis_name', 'analysis_id': analysis_id}
    server_response = server(server_request)
    analysis_name = server_response['name']

    server_request = {'request': 'get_analysis_ranks', 'analysis_id': analysis_id}
    server_response = server(server_request)
    analysis_ranks = server_response['analysis_ranks']

    return HttpResponse(get_template("dendrograms.tmpl").render(Context({'analysis_name': analysis_name,
                                                                         'analysis_id': analysis_id,
                                                                         'ranks': analysis_ranks,
                                                                         'pie_chart_dendrogram_file_prefix': constants.pie_chart_dendrogram_file_prefix,
                                                                         'piechart_dendrograms_dir': os.path.join(analysis_id, constants.pie_charts_dir_name)})))



def analysis_info(request, analysis_id):
    server_request = {'request': 'status'}
    server_response = server(server_request)
    if not server_response:
        return HttpResponse("error when connecting to server: ")
    if analysis_id not in server_response['running_analyses'] + server_response['done_analyses']:
        return HttpResponse("wrong analysis id, server doesn't have anything like this")

    samples_genus_OTUs = get_samples_genus_OTUs(analysis_id)

    server_request = {'request': 'get_sample_map_instances', 'analysis_id': analysis_id}
    sample_map_info = server(server_request)

    server_request = {'request': 'info', 'analysis_id': analysis_id}
    server_response = server(server_request)

    tmpl = get_template("info.tmpl")
    return HttpResponse(tmpl.render(Context({'analysis': server_response, 'sample_map_info': sample_map_info, 'samples_genus_OTUs': samples_genus_OTUs})))


def status_request(request):
    server_request = {'request': 'status'}
    server_response = server(server_request)
    if not server_response:
        return HttpResponse("error when connecting to server: either server is not running or socket name is wrong")
    return HttpResponse("status: %s, running processees: %s" % (server_response['response'], ', '.join(server_response['running_analyses'])))

def exec_env(request):
    if request.method == 'POST':
        form = webforms.EnvUploadForm(request.POST, request.FILES)
        if form.is_valid():
            job_description = form.cleaned_data['job_description']
            time_stamp = helper_functions.get_time_stamp()
            data_file_path = helper_functions.save_uploaded_file(form.cleaned_data['env_file'], time_stamp, output_file_name = constants.data_file_name)

            data_file_sha1sum = helper_functions.get_sha1sum(data_file_path)

            server_request = {'request': 'status'}
            server_response = server(server_request)

            if data_file_sha1sum in server_response['running_analyses']:
                #error we already have it lan
                tmpl = get_template("simple.tmpl")
                return HttpResponse(tmpl.render(Context({'content': "Your ENV file is still being analyzed"})))
            elif data_file_sha1sum in server_response['done_analyses']:
                tmpl = get_template("simple.tmpl")
                return HttpResponse(tmpl.render(Context({'content': "It seems we already have this ENV file analyzed"})))
            # TODO: check validity of the file here..

            server_request = {'request': 'exec_env',
                              'job_description': job_description,
                              'data_file_path': data_file_path,
                              'data_file_sha1sum': data_file_sha1sum}

            server_response = server(server_request)

            if server_response['response'] == 'OK':
                return HttpResponse(get_template("simple.tmpl").render(Context({'content': "Your ENV file is being processed. This is your process id: %s" % server_response['process_id']})))
            else:
                return HttpResponse(get_template("simple.tmpl").render(Context({'content': "something happened"})))
    else:
        form = webforms.EnvUploadForm()

    return HttpResponse(get_template("env_upload_form.tmpl").render(Context({'form': form})))

def update_analysis_remove_samples(request, analysis_id):
    pass

def update_analysis_append_samples(request, analysis_id):

    if request.method == 'POST':

        form = webforms.DataUploadForm(request.POST, request.FILES)

        if form.is_valid():
            time_stamp = helper_functions.get_time_stamp()
            data_file_path = helper_functions.save_uploaded_file(form.cleaned_data['data_file'], time_stamp, output_file_name = constants.data_file_name)

            data_file_sha1sum = helper_functions.get_sha1sum(data_file_path)

            # just send the data file
            server_request = {'request': 'append_samples_to_analysis',
                              'analysis_id': analysis_id,
                              'data_file_path': data_file_path}

            server_response = server(server_request)

            if server_response['response'] == 'OK':
                return HttpResponse(get_template("simple.tmpl").render(Context({'content': "Your request is being processed."})))
            else:
                return HttpResponse(get_template("simple.tmpl").render(Context({'content': "something happened. has no clue. seriously :("})))
        else:
            return HttpResponse(get_template("error.tmpl").render(Context({'content': "Form wasn't valid :( Please click 'back' button of your browser and re-submit the form."})))

    else:
        form = webforms.DataUploadForm()
        tmpl = "data_upload_form.tmpl"

        return HttpResponse(get_template(tmpl).render(Context({'form': form, 'analysis_id': analysis_id})))


def new_analysis(request, analysis_type):

    if request.method == 'POST':

        if analysis_type == "rdp":
            form = webforms.FastaUploadForm(request.POST, request.FILES)
        if analysis_type == "qpcr":
            form = webforms.QpcrUploadForm(request.POST, request.FILES)
        if analysis_type == "env":
            form = webforms.EnvUploadForm(request.POST, request.FILES)

        if form.is_valid():
            job_description = form.cleaned_data['job_description']
            time_stamp = helper_functions.get_time_stamp()
            data_file_path = helper_functions.save_uploaded_file(form.cleaned_data['data_file'], time_stamp, output_file_name = constants.data_file_name)

            data_file_sha1sum = helper_functions.get_sha1sum(data_file_path)

            server_request = {'request': 'status'}
            server_response = server(server_request)

            if data_file_sha1sum in server_response['running_analyses']:
                return HttpResponse(get_template("simple.tmpl").render(Context({'content': "This data file is still being analyzed"})))
            elif data_file_sha1sum in server_response['done_analyses']:
                return HttpResponse(get_template("simple.tmpl").render(Context({'content': "This data file has already been analyzed"})))

            # TODO: check validity of the file here..

            #standard request dict for all analyses.
            server_request = {'request': 'exec_analysis',
                              'analysis_type': analysis_type,
                              'job_description': job_description,
                              'data_file_path': data_file_path,
                              'data_file_sha1sum': data_file_sha1sum}

            #update server request if we're here for rdp analysis
            if analysis_type == "rdp":
                    server_request['seperator'] = form.cleaned_data['seperator']

            server_response = server(server_request)

            if server_response['response'] == 'OK':
                return HttpResponse(get_template("simple.tmpl").render(Context({'content': "Your request is being processed. This is your process id: %s" % server_response['process_id']})))
            else:
                return HttpResponse(get_template("simple.tmpl").render(Context({'content': "something happened. has no clue. seriously :("})))
        else:
            return HttpResponse(get_template("error.tmpl").render(Context({'content': "Form wasn't valid :( Please click 'back' button of your browser and re-submit the form."})))
    else:
        if analysis_type == "rdp":
            form = webforms.FastaUploadForm()
            tmpl = "fasta_upload_form.tmpl"
        if analysis_type == "qpcr":
            form = webforms.QpcrUploadForm()
            tmpl = "qpcr_upload_form.tmpl"
        if analysis_type == "env":
            form = webforms.EnvUploadForm()
            tmpl = "env_upload_form.tmpl"

        return HttpResponse(get_template(tmpl).render(Context({'form': form})))

def about(request):
    tmpl = get_template("about.tmpl")
    return HttpResponse(tmpl.render(Context({'content': "something happened"})))
