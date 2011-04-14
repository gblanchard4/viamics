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
# Rarefaction curve analysis.
#

import os
import sys
from pylab import *
import matplotlib.font_manager
import scipy
import random
import rdp

sys.path.append("../../")
from framework.tools import helper_functions


def get_rarefaction_values(all_species):
    rarefaction_values = [0]
    # from http://www.tnstate.edu/ganter/B412 ExtraRarefaction.html
    N = len(all_species)
    Ni = {}

    rval = 1.0
    for p in range(0, N):
        r = 0.0
        if Ni.has_key(all_species[p]):
            Ni[all_species[p]] += 1
        else:
            Ni[all_species[p]] = 1

        for s in Ni:
            j = p + 1
            rval *= ((N - Ni[s] - j + 1.0) / (N - j + 1.0))
            r += (1 - rval)

        # stuff above is equal to this here:
        #r = 1 - (reduce(operator.mul, [(N - x - j + 1.0) / (N - j + 1.0) for x in Ni.values()]))



        rarefaction_values.append(r)
    return rarefaction_values


def generate_dict(samples_dict, number_of_folds = 15000):
    taxonomic_levels = ['genus', 'family', 'order', 'class', 'phylum']
    samples = helper_functions.sorted_copy(samples_dict.keys())
    rarefaction_dict = {}
    for sample in samples:
        print "sample name: ", sample
        rarefaction_dict[sample] = {}
        for taxonomic_level in taxonomic_levels:
            species_in_the_sample = []
            OTUs = samples_dict[sample][taxonomic_level].keys()

            for i in range(0, len(OTUs)):
                species_in_the_sample += [i] * samples_dict[sample][taxonomic_level][OTUs[i]]

            print "level: ", taxonomic_level, "sequences: ", len(species_in_the_sample), "folds: ", number_of_folds
            rarefaction_values_lists = []

            for i in range(0, number_of_folds):
                random.shuffle(species_in_the_sample)
                rarefaction_values_lists.append(get_rarefaction_values(species_in_the_sample))

            means_and_stdev_tmp  = []
            for i in range(0, len(rarefaction_values_lists[0])):
                means_and_stdev_tmp.append((scipy.mean([x[i] for x in rarefaction_values_lists]), scipy.std([x[i] for x in rarefaction_values_lists])),)
            rarefaction_dict[sample][taxonomic_level] = means_and_stdev_tmp
    return rarefaction_dict

def generate_individual_figures(rarefaction_dict, save_path = None, prefix = "", postfix = ".png", taxonomic_levels = ['genus', 'family', 'order', 'class', 'phylum']):
        taxonomic_level_colors = {'genus': 'red', 'family': 'purple', 'order': 'orange', 'class': 'blue', 'phylum': 'green'}

        for sample in rarefaction_dict:
            fig = figure(figsize=(10, 5))
            rcParams.update({'axes.linewidth' : 0.1})
            rc('grid', color='0.80', linestyle='-', linewidth=0.1)
            grid(True)

            for taxonomic_level in taxonomic_levels:
                if taxonomic_level == taxonomic_levels[0]:
                    plot([x[0] for x in rarefaction_dict[sample][taxonomic_level]], c = taxonomic_level_colors[taxonomic_level], linewidth = 1.2, label = taxonomic_level)
                    plot([x[0] - x[1] for x in rarefaction_dict[sample][taxonomic_level]], ':', c = "black", alpha = 0.9)
                    plot([x[0] + x[1] for x in rarefaction_dict[sample][taxonomic_level]], ':', c = "black", alpha = 0.9)
                else:
                    plot([x[0] for x in rarefaction_dict[sample][taxonomic_level]], c = taxonomic_level_colors[taxonomic_level], alpha = 0.4, label = taxonomic_level)

            seqs = len(rarefaction_dict[sample][taxonomic_level])
            if seqs < 10:
                seqs = 10
            xticks(range(seqs / 10, seqs, seqs / 10), rotation=90, size='xx-small')
            xlim(xmax=seqs)
            yticks(size='xx-small')
            ylabel("Expected # of OTUs for Sample \"%s\" (%d seqs)" % (sample, seqs), fontsize = 'small')

            legend(bbox_to_anchor=(0., 1.02, 1., .102), loc=3, ncol=len(taxonomic_levels), mode="expand", borderaxespad=0., prop = matplotlib.font_manager.FontProperties(size=8))

            if save_path:
                savefig(os.path.join(save_path, prefix + str(sample) + postfix))
            else:
                show()

            fig.clf()
            close('all')


def generate_all_samples_figure(rarefaction_dict, save_path = None, taxonomic_level = "genus"):
        fig = figure(figsize=(10, 5))
        rcParams.update({'axes.linewidth' : 0.1})
        rc('grid', color='0.80', linestyle='-', linewidth=0.1)
        grid(True)

        colors = cm.get_cmap('Dark2', lut=len(rarefaction_dict) + 2)

        i = 0
        for sample in rarefaction_dict:
            plot([x[0] for x in rarefaction_dict[sample][taxonomic_level]], c = colors(i), linewidth = 1, label = sample)
            i +=1

        lens = [len(rarefaction_dict[x]["genus"]) for x in rarefaction_dict]
        lens.sort(reverse = True)
        l = lens[0]
        if l < 10:
            l = 10
        xticks(range(l / 10, l, l / 10), rotation=90, size='xx-small')
        xlim(xmax=l)
        yticks(size='xx-small')
        ylabel("Expected # of OTUs for Samples", fontsize = 'small')

        legend(bbox_to_anchor=(1.01, 1), loc=2, borderaxespad=0., prop = matplotlib.font_manager.FontProperties(size=6))

        if save_path:
            savefig(save_path)
        else:
            show()

        fig.clf()
        close('all')


if __name__ == '__main__':
    def smaller():
        samples_dict = rdp.read_samples_dictionary("./samples_dict")
        sm = {}
        sm["1"] = samples_dict["1"]
        sm["2"] = samples_dict["2"]
        sm["3"] = samples_dict["3"]
        rarefaction_dict = generate_dict(sm)
        save_figures(rarefaction_dict, individual_images = 1)
    def smaller_single():
        samples_dict = rdp.read_samples_dictionary("./samples_dict")
        sm = {}
        sm["1"] = samples_dict["1"]
        sm["2"] = samples_dict["2"]
        sm["3"] = samples_dict["3"]
        rarefaction_dict = generate_dict(sm)
        save_figures(rarefaction_dict, individual_images = 0, save_path = "/tmp/")
    def save_all():
        samples_dict = rdp.read_samples_dictionary("./samples_dict")
        rarefaction_dict = generate_dict(samples_dict)
        rdp.write_samples_dictionary('./rarefaction_dict_50', rarefaction_dict)
        #rarefaction_dict = rdp.read_samples_dictionary("./rarefaction_dict")
        save_figures(rarefaction_dict, individual_images = 1, save_path = "/home/amanda/Desktop/rf/")

    smaller_single()
