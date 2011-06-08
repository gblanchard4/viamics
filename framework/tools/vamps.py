#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (C) 2010 - 2011, A. Murat Eren
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
# This file is used to generate a samples dict from data that was exported from VAMPS.
# An generic file looks like this:
#
#
# ----------------------------
# VAMPS - Taxonomy/Trend Table Analysis; Taxonomic Rank: genus; View Mode: Absolute Number; Threshold: 0%
# Taxonomy / Project--Dataset:	Sample_1	Sample_2	Sample_3	Sample_4
# Bacteria;Actinobacteria;Actinobacteria;Actinomycetales;Actinomycetaceae;Actinomyces	1 	11 	33 	3 
# Bacteria;Actinobacteria;Actinobacteria;Actinomycetales;Actinomycetaceae;Mobiluncus	0 	6 	1 	0 
# Bacteria;Actinobacteria;Actinobacteria;Actinomycetales;Corynebacteriaceae;Corynebacterium	1 	40 	19 	1 
# Bacteria;Actinobacteria;Actinobacteria;Actinomycetales;Micrococcaceae;Micrococcus	0 	1 	0 	0 
# Bacteria;Actinobacteria;Actinobacteria;Actinomycetales;Nocardiaceae;Rhodococcus	0 	0 	2 	0 
# Bacteria;Actinobacteria;Actinobacteria;Actinomycetales;Propionibacteriaceae;Propionibacterium	0 	2 	0 	0 
# Bacteria;Actinobacteria;Actinobacteria;Actinomycetales;Tsukamurellaceae;Tsukamurella	0 	2 	0 	0 
# Bacteria;Actinobacteria;Actinobacteria;Coriobacteriales;Coriobacteriaceae;Atopobium	0 	1 	2 	0 
# Bacteria;Bacteroidetes;Bacteroidia;Bacteroidales;Porphyromonadaceae;Porphyromonas	113 	132 	2791 	1769 
# Bacteria;Bacteroidetes;Bacteroidia;Bacteroidales;Prevotellaceae;Prevotella	47 	131 	399 	285 
# ----------------------------
#

import os
import sys
import cPickle

def create_samples_dictionary(vamps_file):
    """this function reads $vamps_file and parses it to create a sample map from it"""
    samples_dict = {}
    lines = open(vamps_file).readlines()

    samples = extract_sample_names(vamps_file)

    for i in range(0, len(samples)):
        samples_dict[samples[i]] = {'tr': 0, 'species': {}}
        for otu, abundance in [(o.strip().split('\t')[0].split(';')[-1], int(o.strip().split('\t')[i + 1])) for o in lines[2:]]:
            if abundance:
                samples_dict[samples[i]]['species'][otu] = abundance
                samples_dict[samples[i]]['tr'] += abundance

    return samples_dict

def extract_sample_names(vamps_file):
    lines = open(vamps_file).readlines()

    return lines[1].strip().split('\t')[1:]

def get_otu_library(vamps_file):
    lines = open(vamps_file).readlines()
    otu_library = [[o.strip().split('\t')[0].split(';')[-1]] for o in lines[2:]]
    otu_library.sort()
    return otu_library

if __name__ == "__main__":
    pass
