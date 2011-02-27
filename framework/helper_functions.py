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
 
from colorsys import hsv_to_rgb
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


def taxon_colors_dict(p,samples_dict,cm):
    """Return a dict mapping from otu to RGBA color quadruple for each otu in samples_dict """
    if(len(c.ranks[p.type]) > 1):
        return get_structured_taxa_color_dict(p, samples_dict, cm)
    else:
        return get_random_taxa_color_dict(p,samples_dict,cm)


def get_structured_taxa_color_dict(p, samples_dict, cm):
    """Return a dict mapping from otu to RGBA color quadruple for each otu in samples_dict. maintains consistent interface with get_random_taxa_color_dict  """
    return structured_taxa_color_dict(phylo_tree(
                cPickle.load(open(p.files.otu_library_file_path))))


def get_random_taxa_color_dict(p, samples_dict, cm):
    "Return a dict mapping from otu to RGBA color quadruple for each otu in samples_dict. Colors are mapped randomly to taxons. Only used for one-level analyses"
    def getColor(name, n):
        return cm.get_cmap(name, lut=n+2)

    taxa_color_dict = {}

    for rank in c.ranks[p.type]:
        #level_color_dict = {}
        taxons = []
        for sample in samples_dict:
            for taxon in samples_dict[sample][rank]:
                if taxon in taxons:
                    continue
                taxons.append(taxon)

        random.shuffle(taxons)
        colors = getColor('Accent', len(taxons))
        for i in range(0, len(taxons)):
            taxa_color_dict[taxons[i]] = colors(i)

        #taxa_color_dict[rank] = level_color_dict

    return taxa_color_dict

def phylo_tree(otu_library):
    """Return a nested dict (tree) representing the relationships in the taxonomic tree specified by otu_library """
    phylo_tree = {}
    for row in otu_library:
        parent = phylo_tree
        for otu in row:
            if not parent.has_key(otu):
                parent[otu] = {}
            parent = parent[otu]
    return phylo_tree

def phylo_tree_red(otu_library):
    def tree_from(row):
        


def structured_taxa_color_dict(phylo_tree, 
              interval=(0,1),
              saturation=0.2,
              value=0.8,
              alpha=1.0,
              level = None):
    "returns a structured color map for all otus in the phylogenetic tree. Colors are organized so related otus have color hues near each other."
    l = phylo_tree.keys()
    if not l: return {}
    color_spacing = float(interval[1]-interval[0])/len(l)
    def color_dict(current_dict, item):
        rgb = hsv_to_rgb((interval[0]+color_spacing*len(current_dict)),
                                        saturation,
                                        value,
                                        )
        current_dict[item] = (rgb[0], rgb[1], rgb[2], alpha)
        return current_dict
    colors = reduce(color_dict, l, {})
    for i, key in enumerate(l):
        colors.update(structured_taxa_color_dict(phylo_tree[key],
                                                 interval=(interval[0]+i*color_spacing,
                                                           interval[0]+(i+1)*color_spacing),
                                                 saturation=saturation+0.2,
                                                 value=value,
                                                 alpha=alpha
                                                 ))
    return colors
    
    
        
        


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
    return True

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
    prev_isdigit = str[0].isdigit()
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
