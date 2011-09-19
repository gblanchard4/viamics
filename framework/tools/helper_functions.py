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
# Helper data structures and functions for various tasks.
#


import os
import sys
import zlib
import mmap
import time
import copy
import random
import base64
import socket
import string
import hashlib
import cPickle
import re
import traceback

from scipy import log2

sys.path.append("../..")
from framework import constants as c

SerializeToFile     = lambda obj, file: cPickle.dump(obj, open(file, 'w'))
DeserializeFromFile = lambda file: cPickle.load(open(file))
GetCopy             = lambda obj: copy.deepcopy(obj)
RelativePath        = lambda path: path.split(c.analyses_dir)[1].strip("/")

class HeatmapOptions:
    def __init__(self):
        self.abundance_file        = None
        self.sample_color_map_file = None
        self.output_file           = None
        self.category_map_path     = None
        self.scale                 = 'column'
        self.min_percentage        = 0.0
        self.min_present           = 0
        self.log                   = False
        self.width                 = 0
        self.height                = 0
        self.margin_right          = 20
        self.margin_bottom         = 10
        self.cexRow                = 1.5
        self.cexCol                = 1

def server(request):
    """
    #takes a python dict "request", and passes it to the Viamics server through
    #(currently) a UNIX domain socket. 
    #request has at minimum a key "request", whose values can be:
    #                'exec_analysis'                
                     'remove_analysis'              
                     'status'                       
                     'get_analyses'                 
                     'get_analysis_name'            
                     'get_type_of_analysis'         
                     'get_analysis_ranks'           
                     'get_sample_map_name'          
                     'get_sample_maps'              
                     'get_sample_map_instances'     
                     'get_samples_dict_path'        
                     'get_relative_taxon_charts_dir'
                     'get_relative_type_specific_data_dir'
                     'get_otu_confidence_tuples'   
                     'get_otu_t_p_tuples'          
                     'get_samples_in_an_analysis'  
                     'append_samples_to_analysis'  
                     'info'                        
                     'refresh_analysis_files'      
                     'heatmap_options'             
                     'refresh_heatmap'             
                     'refresh_sample_map'          
                     'new_sample_map' 
    #for example:
    #show all analyses:
    server({"request":"get_analyses"}) #returns a listing of all analyses
    #
    #remove given analysis
    server({ 'request': 'remove_analysis', 'analysis_id':             'b7782ab61207929a9e8a2f12eb52b977800d8979-test'})
    #
    #perform analysis:
    server({'request': 'exec_analysis', 'analysis_type': u'rdp',     'job_description': u'fasta', 'seperator': u'_',  'data_file_sha1sum': 'dad183c64f8d0d3516b5cf2c153ab9e97cdf97b4', 'data_file_path': '/home/johnny/Desktop/viamics/framework/tmp/1293740788.36/data_file'})
    #
    #see [the wiki](https://github.com/meren/viamics/wiki/Client-API) for more details
    """
    serversocket = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
    try:
        serversocket.connect(c.socket_name)
    except:
        return {}

    # include a time stamp to the request
    request['time_stamp'] = get_time_stamp()

    serversocket.send(base64.encodestring(zlib.compress(cPickle.dumps(request), 9)))

    data = ""
    while True:
        chunk = serversocket.recv(512)
        data += chunk
        if chunk[-1] == "\n":
            break

    response = cPickle.loads(zlib.decompress(base64.decodestring(data)))
    serversocket.close()

    return response

def get_groups_colors_from_sample_map_file(sample_map_file_path):
    sample_groups = {}
    group_colors = {}

    for row in [l.strip().split('\t') for l in open(sample_map_file_path).readlines()]:
        if sample_groups.has_key(row[1]):
            sample_groups[row[1]].append(row[0])
        else:
            sample_groups[row[1]] = [row[0]]
            group_colors[row[1]] = row[2]

    return (sample_groups, group_colors)


def get_random_taxa_color_dict(p, samples_dict, cm):
    def getColor(name, n):
        return cm.get_cmap(name, lut=n+2)

    taxa_color_dict = {}

    for rank in c.ranks[p.type]:
        level_color_dict = {}
        taxons = []
        for sample in samples_dict:
            for taxon in samples_dict[sample][rank]:
                if taxon in taxons:
                    continue
                taxons.append(taxon)

        random.shuffle(taxons)
        colors = getColor('Accent', len(taxons))
        for i in range(0, len(taxons)):
            level_color_dict[taxons[i]] = colors(i)

        taxa_color_dict[rank] = level_color_dict

    return taxa_color_dict

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



def get_largest_abundance_number_in_all_samples(samples_dict):
    abundance_values = []
    for sample in samples_dict:
        for rank in samples_dict[sample]:
            if rank != "tr":
                for value in samples_dict[sample][rank]:
                    abundance_values.append(samples_dict[sample][rank][value])

    return max(abundance_values)


def create_percent_abundance_file(samples_dict, output_file_path, rank = 'genus'):
    samples = samples_dict.keys()
    names = []
    for name_list in [samples_dict[t][rank].keys() for t in samples_dict]:
        for name in name_list:
            if not name in names:
                names.append(name)

    f = open(output_file_path, 'w')
    f.write("\t".join(["Sample_ID"] + samples) + "\n")
    for name in names:
        abundance_vector = []
        for sample in samples:
            if samples_dict[sample][rank].has_key(name) and samples_dict[sample]['tr'] > 0:
                abundance_vector.append(samples_dict[sample][rank][name] * 100.0 / samples_dict[sample]['tr'])
            else:
                abundance_vector.append(0.0)
        f.write("\t".join([name] + [str(x) for x in abundance_vector]) + "\n")
    f.close()

def se(l):
    """shannon entropy of random variable with probability
    vector l."""
    return sum([-p*log2(p) for p in l if p > 0])

def generate_feature_vectors_from_samples_dict(samples_dict, otu_library, rank = "genus"):
    enum_ranks = {'species': 0, 'phylum': 0, 'class': 1, 'order': 2, 'family': 3, 'genus': 4}
    components = list(set([o[enum_ranks[rank]] for o in otu_library]))
    samples = sorted_copy(samples_dict.keys())

    features = []
    for sample in samples:
        base_vector = [0.0] * len(components)
        for i in range(0, len(components)):
            if samples_dict[sample][rank].has_key(components[i]):
                if samples_dict[sample]['tr'] == 0:
                    base_vector[i] = 0.0
                else:
                    base_vector[i] = samples_dict[sample][rank][components[i]] * 100.0 / samples_dict[sample]['tr']
        features.append(base_vector)

    return samples, components, features


def seqs(f, include_comments = False):
    """A generator for the sequences in a FASTA file"""
    seq = ""
    f = f if include_comments else (l for l in f if not l.startswith(";"))
    for line in f:
        if seq != "" and line.startswith('>'):
            yield seq
            seq = ""
        seq += line
    if seq != "":
        yield seq
################################################################################
#Unifrac export preparation
#the following functions mung data into the necessary shape to use the
#Fast UniFrac webapp
################################################################################
NON_ALPHANUMERIC = re.compile('[\W_]+')
import zipfile

def env_triples(samples_dict, level):
    """A generator of 3-tuples (otu, sample, quantity) for all samples in samples_dict. Level is the taxonomic level (genus, phylum, etc. ) to use for otus"""
    for s_id, sample in samples_dict.iteritems():
        for otu, quant in sample[level].iteritems():
            yield tuple(map(lambda x: NON_ALPHANUMERIC.sub('.',x) if not isinstance(x,(int, long, float)) else x,
                            (otu, s_id, quant)))


def category_map(sample_map_lines, headers):
    """Creates what the UniFrac people call a 'category map' from a Viamics sample_map file.

    A Viamics sample_map file includes several tab-separated columns, the first of which is the sample id.
    headers is a list of pairs (column_number, header_text) where column_number is the column in the sample_map file, and header_text is the name of the column that will be created in the category map.

    The result is an iterator of len(headers)-tuples. The first is simply [text for num,text in headers]"""
    yield tuple([text for num,text in headers])
    for line in sample_map_lines:
        line = line.split('\t')
        yield tuple([NON_ALPHANUMERIC.sub('.',line[h[0]]) for h in headers])

def write_category_map(rows, map_file):
    """writes each row in rows as a tab-separated spreadsheet row to map_file, and closes map_file."""
    rows = iter(rows)
    def _rows():#add '#' to first row for category map format
        r_0 = rows.next()
        r_0 = tuple(('#'+r_0[0],)+r_0[1:])
        yield r_0
        for r in rows:
            yield r
    write_rows(_rows(),map_file)
    

def write_rows(rows, f,delim='\t'):
    z = zipfile.ZipFile(f, 'w',zipfile.ZIP_DEFLATED)
    z.writestr(f.name.split('/')[-1],
               reduce(lambda a,b: a+b, [str.join(delim,map(lambda x: str.strip(str(x)),r))+'\n' for r in rows]))
    z.close()

################################################################################
#End Fast Unifrac tools
################################################################################

def get_fs_compatible_name(fname):
    fname = fname.replace(")", "")
    fname = fname.replace("(", "")
    fname = fname.replace("/", "_")
    fname = fname.replace(" ", "_")
    fname = fname.replace('"', "")
    return fname

def filter_dict(dict, keep_only):
    new_dict = {}
    for i in dict:
        if i in keep_only:
            new_dict[i] = dict[i]
    return new_dict

def get_number_of_lines(file_path):
    f = open(file_path, "r+")
    buf = mmap.mmap(f.fileno(), 0)
    lines = 0
    readline = buf.readline
    while readline():
        lines += 1
    return lines

def get_time_stamp():
    return time.time()

def save_uploaded_file(file_obj, time_stamp, output_file_name = None):
    base_dir = os.path.join(c.temp_files_dir, str(time_stamp))
    if not os.path.exists(base_dir):
        os.makedirs(base_dir)
    file_path = os.path.join(base_dir, output_file_name or file_obj.field_name)

    f = open(file_path, "w")
    for line in file_obj.readlines():
        f.write(line)
    f.close()

    return file_path

def is_qpcr_file_valid(file_path):
    return True

def is_sample_map_valid(file_path):
    return True

def is_fasta_valid(file_path):
    """Checks if a file is a valid FASTA file.
    Viamics only handles nucleotide bases, and doesn't complain about how the
    sequence is laid out in lines as long as it is not broken by any blank ones

    The file will be validated according to the following grammar:
    
    <file>     ::= <token> | <token> <file>
    <token>    ::= <ignore> | <seq>
    <ignore>   ::= <whitespace> | <comment> <newline>
    <seq>      ::= <header> <molecule> <newline>
    <header>   ::= ">" <arbitrary text> <newline>
    <molecule> ::= <base> | <base> <molecule>
    <base>     ::= "^[ACGTURYKMSWBDHVNX-]+$" 
    """

    dna = re.compile("^[ACGTURYKMSWBDHVNX-]+$")
    
    try:
        fas = open(file_path)
    except TypeError:
        fas = file_path

    def ignore(f):
        l = f.readline()
        if l.strip() == '' or l.startswith(';'):
            return True
        else:
            f.seek(-1*len(l),1)#put the line back
            #print l
            return False
            
    def header(f):
        l = f.readline()
        if l.startswith('>'):
            return True
        else:
            f.seek(-1*len(l),1)#put the line back
            #print l
            return False

    def molecule(f):
        l = f.readline()
        valid = False
        while(dna.match(l.strip())):
            valid = True
            l = f.readline()
        f.seek(-1*len(l),1)
        return valid

    def seq(f):
        return header(f) and molecule(f)


    def token(f):
        return ignore(f) or seq(f)

    valid = True
    done = '1'
    while(valid and done != ''):
        done = fas.read(10)
        fas.seek(-1*len(done),1)
        valid = token(fas)
        
    return valid
    
def get_sha1sum(file_path):
    h = hashlib.sha1()
    h.update(open(file_path, "rb").read())
    filehash = h.hexdigest()
    return filehash.lower()

def sorted_copy(alist):
    # inspired by Alex Martelli
    # http://aspn.activestate.com/ASPN/Cookbook/Python/Recipe/52234
    indices = map(_generate_index, alist)
    decorated = zip(indices, alist)
    decorated.sort()
    return [ item for index, item in decorated ]

def _generate_index(str):
    """
    Splits a string into alpha and numeric elements, which
    is used as an index for sorting"
    """
    #
    # the index is built progressively
    # using the _append function
    #
    index = []
    def _append(fragment, alist=index):
        if fragment.isdigit(): fragment = int(fragment)
        alist.append(fragment)

    # initialize loop
    prev_isdigit = False if len(str) == 0 else str[0].isdigit()
    current_fragment = ''
    # group a string into digit and non-digit parts
    for char in str:
        curr_isdigit = char.isdigit()
        if curr_isdigit == prev_isdigit:
            current_fragment += char
        else:
            _append(current_fragment)
            current_fragment = char
            prev_isdigit = curr_isdigit
    _append(current_fragment)    
    return tuple(index)

def get_sample_map_dict(p):
    sample_groups, group_colors = get_groups_colors_from_sample_map_file(p.files.sample_map_file_path)

    heatmaps = {}
    dendrograms = {}
    sample_map_percent_abundance_files = {}

    V = lambda x: vars(p.files)[x]

    for rank in c.ranks[p.type]:
        heatmaps[rank] = RelativePath(V(c.abundance_heatmap_file_prefix + rank + '_file_path'))
        dendrograms[rank] = RelativePath(os.path.join(p.dirs.sample_map_dendrograms_dir, c.pie_chart_dendrogram_file_prefix + rank + '.png'))
        sample_map_percent_abundance_files[rank] = RelativePath(V(c.percent_abundance_file_prefix + rank + '_file_path'))

    original_samples_in_fasta = sorted_copy([sample.strip() for sample in open(p.files.all_unique_samples_file_path).readlines()])
    samples_in_map = [x[0] for x in [l.strip().split('\t') for l in open(p.files.sample_map_file_path).readlines()]]

    included_samples = [sample for sample in original_samples_in_fasta if sample in samples_in_map]
    excluded_samples = [sample for sample in original_samples_in_fasta if sample not in samples_in_map]

    sample_map_dict = {'name'                   : open(p.files.sample_map_name_file_path).read().strip(),
                       'instance'               : p.dirs.sample_map_instance,
                       'ranks'                  : c.ranks[p.type],
                       'included'               : included_samples,
                       'excluded'               : excluded_samples,
                       'heatmaps'               : heatmaps,
                       'dendrograms'            : dendrograms,
                       'shannons'               : RelativePath(os.path.join(p.dirs.sample_map_instance_dir, 'shannons.png')),
                       'simpsons'               : RelativePath(os.path.join(p.dirs.sample_map_instance_dir, 'simpsons.png')),
                       'taxon_charts_dir'       : RelativePath(p.dirs.sample_map_taxon_charts_dir),
                       'percent_abundance_files': sample_map_percent_abundance_files,
                       'sample_groups'          : sample_groups,
                       'group_colors'           : group_colors}

    return sample_map_dict

def confirm(prompt=None, resp=False):
    """courtesy of http://code.activestate.com/recipes/541096/"""
    if prompt is None:
        prompt = 'Confirm'

    if resp:
        prompt = '%s [%s] | %s: ' % (prompt, 'Y', 'n')
    else:
        prompt = '%s [%s] | %s: ' % (prompt, 'N', 'y')

    while True:
        ans = raw_input(prompt)
        if not ans:
            return resp
        if ans not in ['y', 'Y', 'n', 'N']:
            print 'please enter y or n.'
            continue
        if ans == 'y' or ans == 'Y':
            return True
        if ans == 'n' or ans == 'N':
            return False
