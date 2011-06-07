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
# Generates dot plots for every taxon to highlight percent abundance differences in samples in
# sample maps.
#

import os
import math
import numpy
import random as r
import sys
from pylab import *
from cogent.maths.stats.test import t_two_sample as t_test

sys.path.append("../../")
from framework.tools import helper_functions
from framework.tools.rdp import read_samples_dictionary

def log_10_fix(x, pos):
    """The two args are the value and tick position.
    Label ticks with the product of the exponentiation"""
    if x == 0.1:
        return ''
    if x == 1:
        return r'$0$'
    return r'$10^%d$' % int(math.log10(x))

def get_t_p_values_dict_for_subset(samples_dict, otu_library, sample_map_file_path, ranks = None, real_abundance = False):
    """this function sorts OTUs according to students t-test values with expected mean difference of 10. this way
       we get a well sorted OTUs from the ones that have the biggest differnce in terms of percent abundance mean
       to the ones that have smaller difference. Storing this information helps to decide in what order dot plots
       should be shown to the researcher.

       Also OTUs that present in the otu library but have no value within a particular subset of samples are being
       discarded for that subset"""

    otu_t_p_tuples_dict = {}

    # because the way we create otu_library, phylum is the first and genus is the last.
    # opposite of what we have in constants.
    ranks.reverse()

    for rank in ranks:
        sample_groups, group_colors = helper_functions.get_groups_colors_from_sample_map_file(sample_map_file_path)

        temporary_list_of_tuples = []

        for otu in set([o[ranks.index(rank)] for o in otu_library]):
            otu_vectors = {}
            for group in sample_groups.keys():
                otu_vectors[group] = []
                for sample in sample_groups[group]:
                    if samples_dict[sample][rank].has_key(otu):
                        if real_abundance:
                            otu_vectors[group].append(samples_dict[sample][rank][otu])
                        else:
                            if samples_dict[sample]['tr'] == 0:
                                otu_vectors[group].append(0.0)
                            else:
                                otu_vectors[group].append(samples_dict[sample][rank][otu] * 100.0 / samples_dict[sample]['tr'])
                    else:
                        otu_vectors[group].append(0.0)

            #has more than one sample in at least one group (if every group has only one sample t-test would fail)
            has_enough_samples = sum([len(t) - 1 for t in otu_vectors.values()]) > 0

            if sum([sum(v) for v in otu_vectors.values()]) > 0.0:

                sorting_assist = max([numpy.mean(t) for t in otu_vectors.values()])

                # ^^ an OTU is presented at least once in any group
                if len(sample_groups) == 2 and has_enough_samples:
                    # if we have only two groups, go for t-test stuff

                    # t-test fails when there is no variance. ex, t_test([5.0,5.0], [0.0,0.0]) is None, None.
                    # adding a very very small number to all values seemed okay.
                    for vector in otu_vectors.values():
                            vector[0] += r.random() * 1e-6
                    t, p = t_test(otu_vectors.values()[0], otu_vectors.values()[1])
                    temporary_list_of_tuples.append((abs(sorting_assist), otu, t, p),)
                else:
                    # we have more than two groups, just return nothing for now
                    # ANOVA could be used for the rest

                    temporary_list_of_tuples.append((sorting_assist, otu, None, None),)

        otu_t_p_tuples_dict[rank] = []

        # sorting the list based on the temporary sorting assist value
        temporary_list_of_tuples.sort(reverse = 1)

        for tpl in temporary_list_of_tuples:
            otu, otu_fs = tpl[1], helper_functions.get_fs_compatible_name(tpl[1])
            if len(sample_groups) == 2 and has_enough_samples:
                otu_t_p_tuples_dict[rank].append((otu, otu_fs, "%.2f" % tpl[2], "%.2f" % tpl[3]),)
            else:
                otu_t_p_tuples_dict[rank].append((otu, otu_fs, None, None),)

    return otu_t_p_tuples_dict

def generate(samples_dict, otu_t_p_tuples_dict, sample_map_file_path, rank = "genus", save_dir = None, is_transparent = False, real_abundance = False):
    sample_groups, group_colors = helper_functions.get_groups_colors_from_sample_map_file(sample_map_file_path)

    if real_abundance:
        """if we're gonna work with real abundance, we need to find out about the 
        ymax of the y axis. to do that, first, we learn the max abundance, then,
        find out the smallest power of 10 that is larger than max_abundance.."""
        max_abundance = helper_functions.get_largest_abundance_number_in_all_samples(samples_dict)
        max_y = 1
        while 1:
            if max_y > max_abundance:
                break
            max_y *= 10

    for otu in [t[0] for t in otu_t_p_tuples_dict[rank]]:
        plot_dict = {}
        for group in sample_groups.keys():
            plot_dict[group] = []
            for sample in sample_groups[group]:
                if samples_dict[sample][rank].has_key(otu):
                    if real_abundance:
                        plot_dict[group].append([samples_dict[sample][rank][otu], sample],)
                    else:
                        if samples_dict[sample]['tr'] == 0:
                            otu_vectors[group].append(0.0)
                        else:
                            plot_dict[group].append([samples_dict[sample][rank][otu] * 100.0 / samples_dict[sample]['tr'], sample],)
                else:
                    plot_dict[group].append([0.0, sample],)

        fig = figure(figsize=(3, 6))
        if real_abundance:
            ax = axes()

        rcParams['axes.titlesize'] = 12.0
        rcParams['font.size'] = 8.0

        rcParams.update({'axes.linewidth' : 0, 'axes.axisbelow': False})
        rc('grid', color='0.50', linestyle='-', linewidth=0.1)
        grid(True)

        for i in range(0, len(plot_dict)):
            key = plot_dict.keys()[i]

            if real_abundance:
                """if abundance is 0.0, make it 1 so it would look better on log scale"""
                for j in range(0, len(plot_dict[key])):
                    if plot_dict[key][j][0] < 1:
                        plot_dict[key][j][0] = 1.0

            title(otu)

            # scattering the samples in X axis, so it would be easier to see them when there are a bunch of them
            # at the same spot. instead of this, [i] * len(plot_dict[key]) could be used to plot them.
            y_positions =  [((1 - (r.gauss(100, 3) /100)) + i) for x in range(0, len(plot_dict[key]))]

            plot(y_positions, [t[0] for t in plot_dict[key]], 'o', color = group_colors[key], ms = 10, mew = 0.6, alpha = .5)

            b = boxplot([t[0] for t in plot_dict[key]], positions=[i + 0.35], sym=',', widths=0.2)
            setp(b['medians'], color=group_colors[key])
            setp(b['whiskers'], color='black', alpha=0.3)
            setp(b['boxes'], color='black', alpha=0.3)
            setp(b['fliers'], color='black', alpha=0.3)
            setp(b['caps'], color='black', alpha=0.3)
        if real_abundance:
            ax.set_yscale('log')
            formatter = FuncFormatter(log_10_fix)
            ax.yaxis.set_major_formatter(formatter)

            xlim(xmin=-0.75, xmax=len(plot_dict) - 0.15)
            xticks(arange(len(plot_dict)), sample_groups.keys(), rotation=90)
            ylim(ymin=1e-1, ymax=max_y)
        else:
            ylim(ymin=-5, ymax=105)
            xlim(xmin=-0.75, xmax=len(plot_dict) - 0.15)
            xticks(arange(len(plot_dict)), sample_groups.keys(), rotation=90)
            yticks(arange(0, 101, 10))

        if not save_dir:
            show()
        else:
            if real_abundance:
                savefig(os.path.join(save_dir, rank + "_" + helper_functions.get_fs_compatible_name(otu) + '_real_abundance' + '.png'), transparent = is_transparent)
            else:
                savefig(os.path.join(save_dir, rank + "_" + helper_functions.get_fs_compatible_name(otu) + '.png'), transparent = is_transparent)

        # clean memory
        try:
            fig.clf()
        except:
            pass
        close('all')


if __name__ == "__main__":
    # FIXME: unittests should be able to cover these.. it
    # is really unnecessary to do this here.
    samples_dict_path = "/path/to/analysis/samples_dict_serialized"
    sample_map_file_path = "/path/to/analysis/maps/3/sample_map"
    otu_library_file_path = "/path/to/analysis/otu_library"

    samples_dict = read_samples_dictionary(samples_dict_path)
    otu_library = read_samples_dictionary(otu_library_file_path)

    otu_t_p_tuples_dict = get_t_p_values_dict_for_subset(samples_dict, otu_library, sample_map_file_path, ranks = ["species"], real_abundance = True)

    generate(samples_dict, otu_t_p_tuples_dict, sample_map_file_path, rank = "species", save_dir = None, is_transparent = False, real_abundance = True)
