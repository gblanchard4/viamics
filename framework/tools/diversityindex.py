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
import pylab

sys.path.append("../../")
from framework.tools import helper_functions
from framework import constants as const#c is used as a local in this file

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
    
    taxonomic_level = const.ranks[type][-1]

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

    fig = pylab.figure(figsize=(3.5, 6.5))

    pylab.rcParams['axes.titlesize'] = 12.0
    pylab.rcParams['font.size'] = 8.0

    pylab.rcParams.update({'axes.linewidth' : 0, 'axes.axisbelow': False})
    pylab.rc('grid', color='0.50', linestyle='-', linewidth=0.1)
    pylab.grid(True)

    pylab.title(__title)

    keys = helper_functions.sorted_copy(plot_dict.keys())

    for key in keys:
        i = keys.index(key)
        # scattering the samples in X axis, so it would be easier to see them when there are a bunch of them
        # at the same spot. instead of this, [i] * len(plot_dict[key]) could be used to plot them.
        y_positions =  [((1 - (r.gauss(100, 3) /100)) + i) for x in range(0, len(plot_dict[key]))]

        pylab.plot(y_positions, plot_dict[key], 'o', color = group_colors[key], ms = 10, mew = 0.6, alpha = .5)

        b = pylab.boxplot(plot_dict[key], positions=[i + 0.35], sym=',', widths=0.2)
        pylab.setp(b['medians'], color=group_colors[key])
        pylab.setp(b['whiskers'], color='black', alpha=0.3)
        pylab.setp(b['boxes'], color='black', alpha=0.3)
        pylab.setp(b['fliers'], color='black', alpha=0.3)
        pylab.setp(b['caps'], color='black', alpha=0.3)

        pylab.plot([0], [max_val], visible = False)
        pylab.plot([-0.9], [-max_val * 10 / 100], visible = False)
        pylab.plot([i + 0.9], [max_val], visible = False)
        pylab.ylim(ymin=-max_val * 10 / 100, ymax=max_val)
        pylab.xticks(pylab.      arange(len(plot_dict)), keys, rotation=90)

    if not save_dir:
        pylab.show()
    else:
        pylab.savefig(os.path.join(save_dir, method + ".png"))

    # clean memory
    try:
        fig.clf()
    except:
        pass
    pylab.close('all')



def generate(samples_dict, img_save_path = None, data_save_path = None, type = None, method='simpsons'):

    taxonomic_level = const.ranks[type][-1]
    
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

    fig = pylab.figure(figsize=(width, 4))

    pylab.rcParams.update({'axes.linewidth' : 0, 'axes.axisbelow': False})
    pylab.rc('grid', color='0.80', linestyle='-', linewidth=0.1)
    pylab.grid(True)

    pos = pylab.arange(len(samples))+.5
    pylab.bar(pos, samples_diversity_index_list, align='center', color=c, linewidth=0.1)
    pylab.plot([0], [1], '^', visible = False)
    pylab.xticks(pos, samples, rotation=90, size='xx-small')
    pylab.xlim(xmax=len(samples))
    pylab.yticks(size='xx-small')

    pylab.ylabel(lbl, fontsize = 12)

    if img_save_path:
        pylab.savefig(img_save_path)
    else:
        pylab.show()

if __name__ == '__main__':
    samples_dict_path = "/home/amanda/repo/ferris/framework/analyses/5b10a9e7cbaf1e975dffe394520cf9015d1e23aa/samples_dict_serialized"
    samples_dict = rdp.read_samples_dictionary(samples_dict_path)

    generate(samples_dict, type = "rdp", method='shannos')

