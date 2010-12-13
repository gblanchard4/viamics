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
# Module functions for quantitative real-time PCR analyses (see unittests/files
# directory for a qpcr example output).
#


import framework.tools.qpcr

from framework import constants as c
from framework import helper_functions

from framework.tools.logger import debug
from framework.helper_functions import DeserializeFromFile, SerializeToFile, GetCopy

def _exec(p, request_dict):
    p.set_analysis_type("qpcr")

    #extracting sample names from qpcr file
    samples = framework.helper_functions.sorted_copy(framework.tools.qpcr.extract_sample_names(p.files.data_file_path))
    open(p.files.all_unique_samples_file_path, 'w').write('\n'.join(samples) + '\n')
    debug("%d unique samples from QPCR stored in samples file" % len(samples), p.files.log_file)

    samples_dictionary(p)
    otu_library(p)


def _append(p, request_dict):
    #FIXME: well, this function has to be implemented..
    pass

def _module_functions(p, request_dict):
    return {
        'qpcr_01': {'func': samples_dictionary, 'desc': 'Samples dictionary'},
        'qpcr_02': {'func': otu_library, 'desc': 'OTU library'}
    }

def _sample_map_functions(p, request_dict):
    return {
        'qpcr_01': {'func': real_t_test_values_and_probabilities_dict, 'desc': 'Student t-test values and probabilities dictionary'},
        'qpcr_02': {'func': real_dot_plots, 'desc': 'Dot plots with real numbers'},
    }


#######################################
# sample map functions
#######################################

def real_t_test_values_and_probabilities_dict(p):
    samples_dict = DeserializeFromFile(p.files.sample_map_filtered_samples_dict_file_path)
    otu_library  = DeserializeFromFile(p.files.otu_library_file_path)
    debug("Computing t-test and p values w/ real values", p.files.log_file)
    otu_t_p_tuples_dict_real = framework.tools.taxons.get_t_p_values_dict_for_subset(samples_dict, otu_library, p.files.sample_map_file_path, ranks = GetCopy(c.ranks[p.type]), real_abundance = True)
    SerializeToFile(otu_t_p_tuples_dict_real, p.files.sample_map_otu_t_p_tuples_dict_real_file_path)

def real_dot_plots(p):
    samples_dict = DeserializeFromFile(p.files.sample_map_filtered_samples_dict_file_path)
    otu_t_p_tuples_dict_real = DeserializeFromFile(p.files.sample_map_otu_t_p_tuples_dict_real_file_path)
    debug("Generating dot plots w/ real values for sample map...", p.files.log_file)
    for rank in c.ranks[p.type]:
        framework.tools.taxons.generate(samples_dict, otu_t_p_tuples_dict_real, p.files.sample_map_file_path, rank, p.dirs.sample_map_taxon_charts_dir, real_abundance = True)


#######################################
# functions
#######################################

def samples_dictionary(p):
    debug("Computing sample dictionary", p.files.log_file)
    samples_dict = framework.tools.qpcr.create_samples_dictionary(p.files.data_file_path)
    debug("Serializing sample dictionary object", p.files.log_file)
    SerializeToFile(samples_dict, p.files.samples_serialized_file_path)


def otu_library(p):
    debug("Regeneration OTU Library", p.files.log_file)
    otu_library = framework.tools.qpcr.get_otu_library(p.files.data_file_path)
    SerializeToFile(otu_library, p.files.otu_library_file_path)

