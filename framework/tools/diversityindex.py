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
# Shannon and Simpson's diversity indices.
#

import os
import sys
import math
import cPickle
import rdp
import random as r
from pylab import *

sys.path.append("../../")
from framework.tools import helper_functions

def get_shannons_diversity_index(species):
    S = len(species.values())
    N = sum(species.values())

    # if total number of species is 1 -or 0-, there is no diversity to measure.
    if S == 0 or S == 1:
        return 0

    H = -sum([(float(ni)/N) * math.log(float(ni)/N) for ni in species.values()]) - ((S - 1) / (2 * N))

    return H

def get_simpsons_diversity_index(species):
    # species = {'Gardnerella': 4124, 'Paralactobacillus': 1, 'Peptoniphilus': 8, 'Xylanibacter': 1,
    # 'Peptostreptococcus': 19, 'Finegoldia': 5, 'Allisonella': 6, 'Fusobacterium': 10,
    # 'Paraeggerthella': 4, 'Atopobium': 401, 'Gemella': 2, 'Sneathia': 70, 'Anaerococcus': 130,
    # 'Howardella': 11, 'Asaccharobacter': 93, 'Anaeroglobus': 9, 'Prevotella': 298, 'Corynebacterium': 10}
    #simpsons diversity index calculation formula:
    # from http://en.wikipedia.org/wiki/Simpson_index
    total_number_of_species = sum(species.values())

    # if total number of species is 1 -or 0-, there is no diversity to measure.
    if total_number_of_species == 1 or total_number_of_species == 0:
        return 0

    D = 1 - (sum([x*(x-1) for x in species.values()]) / float((long(total_number_of_species) * long(total_number_of_species) - 1)))

    return D

def generate_for_sample_map(samples_dict, sample_map_file_path, save_dir = None, type = None, method='simpsons'):
    taxonomic_level = "genus"
    if type == "qpcr" or type == "env":
        taxonomic_level = "species"

    sample_groups, group_colors = helper_functions.get_groups_colors_from_sample_map_file(sample_map_file_path)

    plot_dict = {}

    for group in sample_groups:
        plot_dict[group] = []
        for sample in sample_groups[group]:
            if method == 'simpsons':
                plot_dict[group].append(get_simpsons_diversity_index(samples_dict[sample][taxonomic_level]))
                __title = "Simpson's Diversity Index"
            if method == 'shannons':
                plot_dict[group].append(get_shannons_diversity_index(samples_dict[sample][taxonomic_level]))
                __title = "Shannon Diversity Index"

    max_val = max([max(l) for l in plot_dict.values()])
    max_val = max_val + max_val * 10 / 100

    fig = figure(figsize=(3.5, 6.5))

    rcParams['axes.titlesize'] = 12.0
    rcParams['font.size'] = 8.0

    rcParams.update({'axes.linewidth' : 0, 'axes.axisbelow': False})
    rc('grid', color='0.50', linestyle='-', linewidth=0.1)
    grid(True)

    title(__title)

    for i in range(0, len(plot_dict)):
        key = plot_dict.keys()[i]

        # scattering the samples in X axis, so it would be easier to see them when there are a bunch of them
        # at the same spot. instead of this, [i] * len(plot_dict[key]) could be used to plot them.
        y_positions =  [((1 - (r.gauss(100, 3) /100)) + i) for x in range(0, len(plot_dict[key]))]

        plot(y_positions, plot_dict[key], 'o', color = group_colors[key], ms = 10, mew = 0.6, alpha = .5)

        b = boxplot(plot_dict[key], positions=[i + 0.35], sym=',', widths=0.2)
        setp(b['medians'], color=group_colors[key])
        setp(b['whiskers'], color='black', alpha=0.3)
        setp(b['boxes'], color='black', alpha=0.3)
        setp(b['fliers'], color='black', alpha=0.3)
        setp(b['caps'], color='black', alpha=0.3)

        ylim(ymin=-max_val * 10 / 100, ymax=max_val)
        xlim(xmin=-0.75, xmax=len(plot_dict) - 0.15)
        xticks(arange(len(plot_dict)), sample_groups.keys(), rotation=90)

    if not save_dir:
        show()
    else:
        savefig(os.path.join(save_dir, method + ".png"))

    # clean memory
    try:
        fig.clf()
    except:
        pass
    close('all')



def generate(samples_dict, img_save_path = None, data_save_path = None, type = None, method='simpsons'):
    #we assume we're working with RDP
    taxonomic_level = "genus"
    #but what if it's not?
    if type == "qpcr" or type == "env":
        taxonomic_level = "species"

    samples = helper_functions.sorted_copy(samples_dict.keys())
    samples_diversity_index_list = []
    if method == 'simpsons':
        samples_diversity_index_list = [get_simpsons_diversity_index(samples_dict[sample][taxonomic_level]) for sample in samples]
        lbl = "Simpson's Sample Diversity Index"
        c = color='#ADADEF'
    elif method == 'shannons':
        samples_diversity_index_list = [get_shannons_diversity_index(samples_dict[sample][taxonomic_level]) for sample in samples]
        lbl = "Shannon Diversity Index"
        c = color='#66AA66'
    else:
        return None

    # store diveristy indices in a text file as well
    if data_save_path:
        f = open(data_save_path, 'w')
        for i in range(0, len(samples)):
            f.write("%s\t%f\n" % (samples[i], samples_diversity_index_list[i]))
        f.close()

    width = len(samples) / 5
    if width < 5:
        width = 5

    if width > 15:
        width = 15

    fig = figure(figsize=(width, 4))

    rcParams.update({'axes.linewidth' : 0, 'axes.axisbelow': False})
    rc('grid', color='0.80', linestyle='-', linewidth=0.1)
    grid(True)

    pos = arange(len(samples))+.5
    bar(pos, samples_diversity_index_list, align='center', color=c, linewidth=0.1)
    plot([0], [1], '^', visible = False)
    xticks(pos, samples, rotation=90, size='xx-small')
    xlim(xmax=len(samples))
    yticks(size='xx-small')

    ylabel(lbl, fontsize = 12)
    
    if img_save_path:
        savefig(img_save_path)
    else:
        show()

if __name__ == '__main__':
    # for testing purposes:
    samples_dict_path = "/path/to/analysis/samples_dict_serialized"
    samples_dict = rdp.read_samples_dictionary(samples_dict_path)
    sample_map_file_path = "/path/to/analysis/maps/1/sample_map"

    generate(samples_dict, method='shannons')
    generate_for_sample_map(samples_dict, sample_map_file_path)
