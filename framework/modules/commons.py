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
# Module independent, common analyses.
#

import copy

from framework import constants as c
from framework.tools import helper_functions

from framework.tools.logger import debug
from framework.helper_functions import HeatmapOptions, DeserializeFromFile, SerializeToFile, GetCopy, RelativePath

import framework.tools.bar
import framework.tools.diversityindex
import framework.tools.piechart
import framework.tools.hcluster
import framework.tools.taxons
import framework.tools.heatmap

import matplotlib.cm as cm


def _exec(p, request_dict):
    sequences_bar_image(p)
    simpsons_diversity_bar_image(p)
    shannon_diversity_bar_image(p)
    random_taxon_colors_dict(p)
    pie_charts(p)
    pie_chart_dendrograms(p)


def _append(p, request_dict):
    """Add the given request_dict to the analysis in p, and generate images that are changed """
    #import pdb; pdb.set_trace()
    #FIXME: This is the worst possible way to handle this request (instead, images for unchanged samples shouldn't be re-created):
    #
    #Here's what I plan to do: each type of analysis has a tool for extracting sample
    #names from a data file.
    #get that list from request_dict.additional_data_file_path, then (maybe) make a
    #modified samples_dict from it containing only the new/modified samples, point
    #point p.samples_serialized_file_path at this new file, and call _exec on p.
    #
    #Thinking about all this makes me wonder what the point of all this disk IO is. Are
    #are the typical data sets large enough that memory use is an issue? Is the program
    #CPU bound enough that the time to read and write is irrelevant?
    _exec(p, request_dict)


def _module_functions(p, request_dict):
    return {
        'commons_01': {'func': sequences_bar_image, 'desc': 'Number of sequences bar image'},
        'commons_02': {'func': simpsons_diversity_bar_image, 'desc': 'Simpsons diversity image'},
        'commons_03': {'func': shannon_diversity_bar_image, 'desc': 'Shannon diversity image'},
        'commons_04': {'func': random_taxon_colors_dict, 'desc': 'Random taxon colors'},
        'commons_05': {'func': pie_charts, 'desc': 'Pie charts'},
        'commons_06': {'func': pie_chart_dendrograms, 'desc': 'Pie chart dendrograms'},
    }

def _sample_map_functions(p, request_dict):
    return {
        'commons_01': {'func': t_test_values_and_probabilities_dict, 'desc': 'Student t-test values and probabilities dictionary'},
        'commons_02': {'func': dot_plots, 'desc': 'Dot plot figures for OTUs'},
        'commons_03': {'func': heatmaps, 'desc': 'Heatmap figures'},
        'commons_04': {'func': sample_dendrograms, 'desc': 'Sample dendrograms'},
        'commons_05': {'func': shannon_diversity_dot_plot, 'desc': 'Shannon diversity dot plot'},
        'commons_06': {'func': simpsons_diversity_dot_plot, 'desc': 'Simpsons diversity dot plot'},
    }


#######################################
# sample map functions
#######################################

def t_test_values_and_probabilities_dict(p):
    samples_dict = DeserializeFromFile(p.files.sample_map_filtered_samples_dict_file_path)
    otu_library  = DeserializeFromFile(p.files.otu_library_file_path)
    debug("Generating t-test values and probabilities dict", p.files.log_file)
    otu_t_p_tuples_dict = framework.tools.taxons.get_t_p_values_dict_for_subset(samples_dict, otu_library, p.files.sample_map_file_path, ranks = GetCopy(c.ranks[p.type]))
    SerializeToFile(otu_t_p_tuples_dict, p.files.sample_map_otu_t_p_tuples_dict_file_path)

def dot_plots(p):
    samples_dict = DeserializeFromFile(p.files.sample_map_filtered_samples_dict_file_path)
    otu_t_p_tuples_dict = DeserializeFromFile(p.files.sample_map_otu_t_p_tuples_dict_file_path)
    for rank in c.ranks[p.type]:
        #taxon charts
        debug("Generating dot plots for '%s' level" % rank, p.files.log_file)
        framework.tools.taxons.generate(samples_dict, otu_t_p_tuples_dict, p.files.sample_map_file_path, rank, p.dirs.sample_map_taxon_charts_dir)

def heatmaps(p):
    samples_dict = DeserializeFromFile(p.files.sample_map_filtered_samples_dict_file_path)
    for rank in c.ranks[p.type]:
        debug("Creating percent abundance for '%s' level" % rank, p.files.log_file)
        percent_abundance_file_path = vars(p.files)[c.percent_abundance_file_prefix + rank + '_file_path']
        framework.helper_functions.create_percent_abundance_file(samples_dict, percent_abundance_file_path, rank = rank)

        # heatmaps
        heatmap_options = copy.deepcopy(HeatmapOptions())
        heatmap_options.abundance_file = RelativePath(percent_abundance_file_path)
        heatmap_options.sample_color_map_file = RelativePath(p.files.sample_map_file_path)
        heatmap_options.output_file = RelativePath(vars(p.files)[c.abundance_heatmap_file_prefix + rank + '_file_path'])
        debug("Creating percent abundance heatmap for '%s' level" % rank, p.files.log_file)
        SerializeToFile(heatmap_options, vars(p.files)[c.heatmap_options_file_prefix + rank + '_file_path'])
        framework.tools.heatmap.main(heatmap_options, c.analyses_dir)

def sample_dendrograms(p):
    samples_dict = DeserializeFromFile(p.files.sample_map_filtered_samples_dict_file_path)
    debug("Generating dendrograms for sample map...", p.files.log_file)
    framework.tools.hcluster.generate(samples_dict,
                                            DeserializeFromFile(p.files.otu_library_file_path),
                                            pie_charts_dir = p.dirs.pie_charts_dir,
                                            dendrogram_prefix = c.pie_chart_dendrogram_file_prefix,
                                            save_dir = p.dirs.sample_map_dendrograms_dir,
                                            map = helper_functions.get_sample_map_dict(p),
                                            ranks = GetCopy(c.ranks[p.type]))

def shannon_diversity_dot_plot(p):
    samples_dict = DeserializeFromFile(p.files.sample_map_filtered_samples_dict_file_path)
    debug("Generating diversity index images...", p.files.log_file)
    framework.tools.diversityindex.generate_for_sample_map(samples_dict, p.files.sample_map_file_path, save_dir = p.dirs.sample_map_instance_dir, type = p.type, method = "shannons")

def simpsons_diversity_dot_plot(p):
    samples_dict = DeserializeFromFile(p.files.sample_map_filtered_samples_dict_file_path)
    debug("Generating diversity index images...", p.files.log_file)
    framework.tools.diversityindex.generate_for_sample_map(samples_dict, p.files.sample_map_file_path, save_dir = p.dirs.sample_map_instance_dir, type = p.type, method = "simpsons")

#######################################
# module functions
#######################################

def sequences_bar_image(p):
    samples_dict = DeserializeFromFile(p.files.samples_serialized_file_path)
    debug("Generating number of sequences bar image", p.files.log_file)
    samples = framework.helper_functions.sorted_copy(samples_dict.keys())
    framework.tools.bar.generate([(sample, samples_dict[sample]['tr']) for sample in samples], p.images.samples_sequences_bar_path)

def simpsons_diversity_bar_image(p):
    samples_dict = DeserializeFromFile(p.files.samples_serialized_file_path)
    debug("Generating Simpson's diversity index image", p.files.log_file)
    framework.tools.diversityindex.generate(samples_dict, p.images.simpsons_diversity_index_img_path, p.files.simpsons_diversity_index_data_path, p.type)

def shannon_diversity_bar_image(p):
    samples_dict = DeserializeFromFile(p.files.samples_serialized_file_path)
    debug("Generating shannons diversity index image", p.files.log_file)
    framework.tools.diversityindex.generate(samples_dict, p.images.shannon_diversity_index_img_path, p.files.shannon_diversity_index_data_path,  p.type, method = "shannons")

def random_taxon_colors_dict(p):
    samples_dict = DeserializeFromFile(p.files.samples_serialized_file_path)
    debug("Generating random taxon color dicts", p.files.log_file)
    taxa_color_dict = framework.helper_functions.get_random_taxa_color_dict(p, samples_dict, cm)
    SerializeToFile(taxa_color_dict, p.files.taxa_color_dict_file_path)

def pie_charts(p):
    samples_dict = DeserializeFromFile(p.files.samples_serialized_file_path)
    debug("Generating piecharts", p.files.log_file)
    framework.tools.piechart.main(samples_dict, DeserializeFromFile(p.files.taxa_color_dict_file_path), ranks = GetCopy(c.ranks[p.type]), pie_chart_file_prefix = c.pie_chart_file_prefix, save_dir = p.dirs.pie_charts_dir)

def pie_chart_dendrograms(p):
    samples_dict = DeserializeFromFile(p.files.samples_serialized_file_path)
    debug("Generating piechart dendrograms", p.files.log_file)
    framework.tools.hcluster.generate(samples_dict, DeserializeFromFile(p.files.otu_library_file_path), pie_charts_dir = p.dirs.pie_charts_dir, dendrogram_prefix = c.pie_chart_dendrogram_file_prefix, ranks = GetCopy(c.ranks[p.type]))


