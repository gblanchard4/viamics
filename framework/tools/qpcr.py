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
# Functions for QPCR module.
#

import os
import sys
import cPickle

def create_samples_dictionary(qpcr_file):
    """this function reads $qpcr_file and parses it to create a sample map from it"""
    samples_dict = {}
    lines = open(qpcr_file).readlines()

    species_array = [s.strip() for s in lines[0].split("\t")[1:]]

    for line in lines[1:]:
        sample = line.split("\t")[0]
        abundances = [int(float(a.strip())) for a in line.split("\t")[1:]]

        temp_dict = {}
        for i in range(0, len(species_array)):
            if abundances[i]:
                temp_dict[species_array[i]] = abundances[i]

        samples_dict[sample] = {'tr': sum(abundances), 'species': temp_dict}

    return samples_dict

def extract_sample_names(qpcr_file):
    lines = open(qpcr_file).readlines()

    return [line.split("\t")[0] for line in lines[1:]]

def get_otu_library(qpcr_file):
    lines = open(qpcr_file).readlines()
    otu_library = [[s.strip()] for s in lines[0].split("\t")[1:]]
    otu_library.sort()
    return otu_library

if __name__ == "__main__":
    pass
