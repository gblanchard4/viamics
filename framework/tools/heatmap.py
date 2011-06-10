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
# Heatmap generator.
#
# This application could be used like this, too:
#
#  python generate_rpy_heatmap.py -a ABUNDANCE_FILE -p 10 -m 1 --row-text-size=1.5 --column-text-size=1 --margin-right=20 --margin-bottom=10 --width=1000 --height=1200 -l
#

import os
import sys
import math
import numpy
import Numeric

from rpy2 import robjects
import rpy2.robjects.numpy2ri
from rpy2.robjects.packages import importr

from optparse import OptionParser

def main(options, analyses_dir = ''):
    if len(analyses_dir):
        sample_color_map_file = os.path.join(analyses_dir, options.sample_color_map_file)
        abundance_file = os.path.join(analyses_dir, options.abundance_file)
        options.output_file = os.path.join(analyses_dir, options.output_file)
    else:
        abundance_file = options.abundance_file
        sample_color_map_file = options.sample_color_map_file

    #first line of the abundance file to see what sample names are
    col_names = open(abundance_file).readline().strip().split("\t")[1:]

    #creating an entry for every bacterium in the abundance file
    row_names_non_scaled = []
    exprs_non_scaled = []
    row_names = []
    exprs = []
    for line in open(abundance_file).readlines()[1:]:
        row_names_non_scaled.append(line.strip().split("\t")[0])
        exprs_non_scaled.append(map(float, line.strip().split("\t")[1:]))


    for i in range(0, len(row_names_non_scaled)):
        if sum(exprs_non_scaled[i]) > options.min_percentage and len([x for x in exprs_non_scaled[i] if x > 0.0]) > options.min_present:
            if options.log:
                exprs.append([math.log10(x + 1) for x in exprs_non_scaled[i]])
                row_names.append(row_names_non_scaled[i])
            else:
                exprs.append(exprs_non_scaled[i])
                row_names.append(row_names_non_scaled[i])
        else:
            print "* Discarding '%s' (total percentage: %f, present in %d sample(s))." % (row_names_non_scaled[i], sum(exprs_non_scaled[i]), len([x for x in exprs_non_scaled[i] if x > 0.0]))

    print "\n%i samples, %i bacteria\n" % (len(col_names), len(row_names))

    data_matrix = numpy.array(exprs)


    sample_color_map = {}
    if sample_color_map_file:
        for sample, desc, color in [x.strip().split('\t') for x in open(sample_color_map_file).readlines() if len(x.strip().split('\t')) == 3]:
            sample_color_map[sample] = {'description': desc, 'color': color}

    def sample_colour(sample_id):
        if sample_color_map.has_key(sample_id):
            return sample_color_map[sample_id]['color']
        else:
            return '#FFFFFF'

    if len(col_names) < 2 or len(row_names) < 2:
        raise Exception, "Number of columns or rows can't be smaller than 2 in a heatmap (you might have enetered some criteria that eliminates all OTU's or samples)."

    #bioDist = importr('bioDist')
    

    generate_heatmap(options, col_names, row_names, data_matrix, sample_colours = map(sample_colour, col_names))#,dist_func=bioDist.spearman_dist

    return


def generate_heatmap(options, col_names, row_names, data_matrix, sample_colours, dist_func=robjects.r.dist):
    robjects.r.library('gplots')
    grdevices = importr('grDevices')

    h = options.height or len(row_names) * 25
    if h < 400:
        h = 400
    w = options.width or len(col_names) * 20
    if w < 500:
        w = 500

    grdevices.png(options.output_file, width=w, height=h)

    robjects.r.heatmap(data_matrix,
                       labRow=row_names,
                       scale=options.scale,
                       labCol=col_names,
                       ColSideColors=robjects.StrVector(sample_colours),
                       col=robjects.r.redgreen(100),
                       distfun=dist_func,
                       key=True,
                       symkey=False,
                       density_info="none",
                       trace="none",
                       margins=robjects.r.c(options.margin_bottom, options.margin_right), # margin right and bottom
                       cexRow=options.cexRow,       # Y axis text size
                       cexCol=options.cexCol)       # X axis text size

    grdevices.dev_off()

    return


if __name__ == "__main__":
    parser = OptionParser()

    parser.add_option("-a", "--abundance-file", dest="abundance_file",
                              type="string", help="abundance file name", metavar="FILE")
    parser.add_option("-c", "--sample-color-map-file", dest="sample_color_map_file",
                              type="string", help="sample color map file. every line should have three columns: SAMPLE ONE_WORD_SAMPLE_DESCRIPTION COLOR", metavar="FILE")
    parser.add_option("-o", "--output-file", dest="output_file", default="heatmap.png",
                              help="file name for the PNG", metavar="FILE")
    parser.add_option("-s", "--scale", dest="scale", default="column",
                              help="scale either columns or rows", metavar="[row|column]")
    parser.add_option("-m", "--min-percentage", dest="min_percentage", type="float", default=0.0,
                              help="minimum total percentage of a bug in all samples (can be bigger than 100%%)")
    parser.add_option("-p", "--min-present", dest="min_present", type="int", default=0,
                              help="minimum total number of samples have this bug (if it present in less than --min-present samples, bug would be discarded)")
    parser.add_option("-l", "--log", dest="log", default=False, action="store_true",
                              help="apply log10 to abundance percentages (log(abundance percentage + 1))")
    parser.add_option("--width", type="int", dest="width", default=0,
                              help="width of the heatmap image (pixels)")
    parser.add_option("--height", type="int", dest="height", default=0,
                              help="height of the heatmap image (pixels)")
    parser.add_option("--margin-right", type="int", dest="margin_right", default=20,
                              help="text area between the map and the right side of the image")
    parser.add_option("--margin-bottom", type="int", dest="margin_bottom", default=10,
                              help="text area between the map and the bottom of the image")
    parser.add_option("--row-text-size", type="float", dest="cexRow", default=1.5,
                              help="row text size")
    parser.add_option("--column-text-size", type="float", dest="cexCol", default=1,
                              help="column text size")

    (options, args) = parser.parse_args()

    if options.abundance_file == None:
        print "Error: You need to provide an input file (percent or total count abundance file)\n"
        parser.print_help()
        sys.exit(2)

    main(options)

