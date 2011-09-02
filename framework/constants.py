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
# Decleration of constant variables.
#

import sys

try:
    import config
except:
    print "config.py is missing. You may create it by copying config-default.py as config.py. New config.py should be edited as well."
    sys.exit(-1)

from os.path import join


#################################################################
# reading variables from config.py
#################################################################
try:
    base_dir = config.base_dir
except AttributeError:
    print "'base_dir' needs to be defined in config.py"
    sys.exit(-1)

try:
    rdp_running_path = config.rdp_running_path
except AttributeError:
    print "'rdp_running_path' needs to be defined in config.py"
    sys.exit(-1)

uchime_running_path = config.uchime_running_path if config.uchime_running_path else ''



#################################################################
# constant values (you shouldn't edit these unless you know what
# you are doing) (any edit here might require some other edits
# for unittests to run properly):
#################################################################


analyses_dir = join(base_dir, "analyses")
error_logs_dir = join(base_dir, "errors")
temp_files_dir = join(base_dir, "tmp")
blastdb_dir = join(base_dir, 'blastdb')

socket_name = join(temp_files_dir, "sock")

web_dir = join(base_dir, "clients/ferrisweb")
web_statics_dir = join(web_dir, "static")
templates_dir = join(web_dir, "templates")


ranks = {}
ranks['rdp'] = ['genus', 'family', 'order', 'class', 'phylum']
ranks['qpcr'] = ['species']
ranks['env'] = ['species']
ranks['vamps'] = ['species']
ranks['blast'] = ['species'] #for now

#rdp
rdp_output_file_name          = "rdp_output"
rdp_error_log_file_name       = "rdp_error_log"
samples_serialized_file_name  = "samples_dict_serialized"
all_unique_samples_file_name  = "unique_sample_names"
otu_library_file_name         = "otu_library"
taxa_color_dict_file_name     = "taxa_color_dict"
low_confidence_seqs_file_name = 'low_confidence_seqs'
threshold_file_name           = 'confidence_threshold'

#general data files
env_file_name = 'sampleIDmap.zip'
data_file_name = "data_file"
data_comment_file_path = "data_comments"
seperator_file_name = "seperator"
job_name_file_name = "job"
log_file_name = "log"
type_of_analysis_file_name = "type_of_analysis"

#images
samples_sequences_bar_name = "samples_sequences_bar.png"
simpsons_diversity_index_img_name = "simpsons_diversity_index.png"
simpsons_diversity_index_data_name = "simpsons_diversity_index.txt"
shannon_diversity_index_img_name = "shannon_diversity_index.png"
shannon_diversity_index_data_name = "shannon_diversity_index.txt"
pie_chart_dendrogram_file_prefix = "piechart_dendrogram_"

#type specific figures dir
type_specific_figures_dir_name = "type_specific_figures"

#pie charts
pie_charts_dir_name = "piecharts"
pie_chart_file_prefix = "piechart_"

#rarefaction stuff (file format is prefix + sample_name + .png)
number_of_folds_for_rarefaction_curves = 100
rarefaction_curves_dir_name = "rarefaction"
rarefaction_curve_file_prefix = "rarefaction_"
rarefaction_curve_file_postfix = ".png"
rarefaction_curves_all_samples_file_name = rarefaction_curve_file_prefix + "all_samples" + rarefaction_curve_file_postfix
rarefaction_dict_serialized_file_name = "rarefaction_dict"

#sample map files and dirs
sample_maps_dir_name = "maps"
sample_map_heatmaps_dir_name = "heatmaps"
sample_map_dendrograms_dir_name = "dendrograms"
sample_map_taxon_charts_dir_name = "taxon_charts"
sample_map_name_file_name = "map_name"
sample_map_file_name = "sample_map"
category_map_file_name = "categoryMap.zip"
sample_map_filtered_samples_dict_file_name = "filtered_samples_dict_serialized"
sample_map_otu_t_p_tuples_dict_file_name = "otu_t_p_tuples_dict"
sample_map_otu_t_p_tuples_dict_real_file_name = "otu_t_p_tuples_real_dict" #for qpcr

percent_abundance_file_prefix = "percent_abundance_"
abundance_heatmap_file_prefix = "abundance_heatmap_"
heatmap_options_file_prefix = "heatmap_options_"

#blast
blast_error_name = "blast_error"
blast_output_name = 'blast_output'
blast_legend_file_extension = '.blg'
blast_db_name_path = 'db_name'
blast_number_of_threads = 4
