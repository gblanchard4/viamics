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
# Piechart generator.
#

from random import shuffle
from pylab import *
import cPickle
import os

import rdp

sys.path.append("../../")
from framework import helper_functions


def generate(samples_dict, taxa_color_dict, rank = "genus", pie_chart_file_prefix = "piechart_", save_dir = None, is_transparent = False):
    """Creates and saves piecharts showing the relative frequency of the different otus in each sample in samples_dict, using the colors in taxa_color_dict to color the piecharts
    
    REQUIRED ARGUMENTS:
    --samples_dict - the dictionary of sample name -> dictionary, created by
                     modules.<analysis type>.samples_dictionary(p)
    --taxa_colors_dict - a dict of OTU name -> rgb or rgba color tuple, used to color the piechart

    OPTIONAL ARGUMENTS:
    --rank="genus" - the level at which to draw the piechart, e.g. rank="phylum" will
    generate piecharts showing the phyla in each sample
    --pie_chart_file_prefix = "piechart_" - Piecharts will be named:  pie_chart_file_prefix + rank + "_" + sample + '.png' and saved in save_dir if save_dir is not None
    --save_dir - location to save piecharts. If not given, attempts to display them"""
    def _generate(mini = False):
        for sample in samples_dict:
            if mini:
                fig = figure(figsize=(3,2))
                ax = axes([0.0, 0.01, 0.66, 0.99])
            else:
                fig = figure(figsize=(4,4))
                ax = axes([0.1, 0.1, 0.7, 0.7])

            rcParams['axes.titlesize'] = 12.0
            rcParams['font.size'] = 6.0

            labels = []
            percentages = []
            c = []

            for taxon in samples_dict[sample][rank]:
                if samples_dict[sample]['tr'] > 0:
                    percentage = samples_dict[sample][rank][taxon] * 100.0 / samples_dict[sample]['tr']
                else:
                    percentage = 100.0
                percentages.append(percentage)
                c.append(taxa_color_dict[rank][taxon])
                if percentage > 5:
                    labels.append(taxon)
                else:
                    labels.append('')

            if mini:
                pie(percentages, shadow=False, colors=c)
            else:
                pie(percentages, labels=labels, shadow=False, colors=c)

            if mini:
                fig.text(0.63, 0.50, sample, verticalalignment='center', fontsize=12)

            else:
                title(sample)

            if not save_dir:
                show()
            else:
                if mini:
                    savefig(os.path.join(save_dir, "mini_" + pie_chart_file_prefix + rank + "_" + sample + '.png'), transparent = is_transparent)
                else:
                    savefig(os.path.join(save_dir, pie_chart_file_prefix + rank + "_" + sample + '.png'), transparent = is_transparent)

            fig.clf()
            close('all')

    _generate()
    _generate(mini = True)


def main(samples_dict, taxa_color_dict, ranks, pie_chart_file_prefix = "piechart_", save_dir = None, otu_library = None, is_transparent = False):
    for rank in ranks:
        generate(samples_dict, taxa_color_dict, rank = rank, pie_chart_file_prefix = pie_chart_file_prefix, save_dir = save_dir, is_transparent = is_transparent)


if __name__ == "__main__":
    samples_dict = rdp.read_samples_dictionary("../analyses/660ec9c89d34f3133e0c1c1ac2bbb39fcb47386f/samples_dict_serialized")
    otu_library = rdp.read_samples_dictionary("../analyses/660ec9c89d34f3133e0c1c1ac2bbb39fcb47386f/otu_library")
    taxa_color_dict = rdp.read_samples_dictionary("../analyses/660ec9c89d34f3133e0c1c1ac2bbb39fcb47386f/taxa_color_dict")
    main(samples_dict, taxa_color_dict, otu_library = otu_library)
    #main(samples_dict, "./files", "tmp_piechart_", "./files/tmp", is_transparent = True)
    #main(samples_dict, "./files")
