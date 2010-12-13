#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
import sys
import cPickle

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
# This file is used to generate a samples dict from a UniFrac environment file. Which has this format:
# 
# (...)
# 58380	72	2
# 137054	76	1
# 55342	74	1
# 11382	155	146
# 11382	157	257
# 11382	156	602
# 11382	159	28
# 11382	60	3
# 11382	61	120
# 11382	62	60
# (...)
#
# where, the first column is otu id, second is sample id and the third one is number of otu id found in the given sample.
#


#ever growing species names for GreenGenes id numbers (if there is a name for an id,
# name will be seen in all figures instead of the GreenGenes id number):
species_pretty_names = {
        '107485': 'L. mucosae',
        '107854': 'L. casei',
        '108027': 'L. brevis',
        '130403': 'L. iners',
        '178564': '178564',
        '180091': 'Incertae sedis',
        '187332': 'L. reuteri',
        '193690': '193690',
        '21096': 'L. crispatus',
        '21772': 'L. vaginalis',
        '51715': 'L. jensenii',


        '104511': 'P. 104511',
        '107329': 'P. nigrescens',
        '108139': 'P. multiformis',
        '114946': 'P. nanceiensis',
        '130804': 'P. buccalis',
        '134265': 'P. 134265',
        '190891': 'P. 190891',
        '198806': 'P. 198806',
        '2200': 'P. albensis',
        '25004': 'P. 25004',
        '31856': 'P. bryantii',
        '36896': 'P. loescheii',
        '56320': 'P. baroniae 56320',
        '68416': 'P. 68416',
        'None': 'None',

        '133171': 'M. rRNA031',
        '169931': 'M. NCBI 77133',
        '87238': 'M. micrinuciformis',
        }

def create_samples_dictionary(env_file):
    """this function reads $env_file and parses it to create a sample map from it"""
    samples_dict = {}
    lines = open(env_file).readlines()

    for line in lines:
        species = line.split("\t")[0]

        if species_pretty_names.has_key(species):
            species = species_pretty_names[species]

        sample = line.split("\t")[1]
        abundance = int(line.split("\t")[2].strip())

        if samples_dict.has_key(sample):
            samples_dict[sample]['species'][species] = abundance
        else:
            samples_dict[sample] = {}
            samples_dict[sample]['species'] = {species: abundance}

    for sample in samples_dict:
        samples_dict[sample]['tr'] = sum(samples_dict[sample]['species'].values())

    return samples_dict

def extract_sample_names(env_file):
    lines = open(env_file).readlines()

    return list(set([line.split("\t")[1] for line in lines]))

def get_otu_library(env_file):
    lines = open(env_file).readlines()

    otus_list = list(set([line.split("\t")[0] for line in lines]))

    for i in range(0, len(otus_list)):
        if species_pretty_names.has_key(otus_list[i]):
            otus_list[i] = species_pretty_names[otus_list[i]]

    otu_library = [[x] for x in otus_list]
    otu_library.sort()

    return otu_library

if __name__ == "__main__":
    s = create_samples_dictionary("files/sample_env_output")
    n = extract_sample_names("files/sample_env_output")
    o = get_otu_library("files/sample_env_output")

    for i in s:
        print i, s[i]["species"]

