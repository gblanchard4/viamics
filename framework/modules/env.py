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
# Module functions for environment file analyses (see unittests/files directory for an
# environment file).
#


import framework.tools.env

from framework import constants as c
from framework.tools import helper_functions

from framework.tools.logger import debug
from framework.tools.helper_functions import DeserializeFromFile, SerializeToFile, GetCopy

def _exec(p, request_dict):
    p.set_analysis_type("env")

    #extracting sample names from env file
    samples = framework.tools.helper_functions.sorted_copy(framework.tools.env.extract_sample_names(p.files.data_file_path))
    open(p.files.all_unique_samples_file_path, 'w').write('\n'.join(samples) + '\n')
    debug("%d unique samples from ENV stored in samples file" % len(samples), p.files.log_file)

    samples_dictionary(p)
    otu_library(p)


def _append(p, request_dict):
    pass


def _module_functions(p, request_dict):
    return {
            'env_01': {'func': samples_dictionary, 'desc': 'Samples dictionary'},
            'env_02': {'func': otu_library, 'desc': 'OTU library'}
    }

def _sample_map_functions(p, request_dict):
    return {}


#######################################
# functions
#######################################

def samples_dictionary(p):
    debug("Computing sample dictionary", p.files.log_file)
    samples_dict = framework.tools.env.create_samples_dictionary(p.files.data_file_path)
    debug("Serializing sample dictionary object", p.files.log_file)
    helper_functions.SerializeToFile(samples_dict, p.files.samples_serialized_file_path)


def otu_library(p):
    debug("Regeneration OTU Library", p.files.log_file)
    otu_library = framework.tools.env.get_otu_library(p.files.data_file_path)
    SerializeToFile(otu_library, p.files.otu_library_file_path)
