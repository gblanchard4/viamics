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
# Code for hierarchical clustering. Modified from
# Programming Collective Intelligence by Toby Segaran.
#

import os
import sys
sys.path.append("../..")

from numpy import *
from PIL import Image, ImageDraw

from framework.helper_functions import generate_feature_vectors_from_samples_dict
import framework.constants

class cluster_node:
    def __init__(self, vec, left = None, right = None, distance = 0.0, id = None, count = 1):
        self.left = left
        self.right = right
        self.vec = vec
        self.id = id
        self.distance = distance
        self.count = count #only used for weighted average 

def L2dist(v1, v2):
    return sqrt(sum((v1 - v2)**2))

def L1dist(v1, v2):
    return sum(abs(v1 - v2))

# def Chi2dist(v1, v2):
#     return sqrt(sum((v1 - v2)**2))

def hcluster(features, distance = L2dist):
    #cluster the rows of the "features" matrix
    distances = {}
    currentclustid =  - 1

    # clusters are initially just the individual rows
    clust = [cluster_node(array(features[i]), id = i) for i in range(len(features))]

    while len(clust)>1:
        lowestpair = (0, 1)
        closest = distance(clust[0].vec, clust[1].vec)

        # loop through every pair looking for the smallest distance
        for i in range(len(clust)):
            for j in range(i + 1, len(clust)):
                # distances is the cache of distance calculations
                if (clust[i].id, clust[j].id) not in distances: 
                    distances[(clust[i].id, clust[j].id)] = distance(clust[i].vec, clust[j].vec)

                d = distances[(clust[i].id, clust[j].id)]

                if d<closest:
                    closest = d
                    lowestpair = (i, j)

        # calculate the average of the two clusters
        mergevec = [(clust[lowestpair[0]].vec[i] + clust[lowestpair[1]].vec[i])/2.0 \
            for i in range(len(clust[0].vec))]

        # create the new cluster
        newcluster = cluster_node(array(mergevec), left = clust[lowestpair[0]], 
                             right = clust[lowestpair[1]], 
                             distance = closest, id = currentclustid)

        # cluster ids that weren't in the original set are negative
        currentclustid -= 1
        del clust[lowestpair[1]]
        del clust[lowestpair[0]]
        clust.append(newcluster)

    return clust[0]


def extract_clusters(clust, dist):
    # extract list of sub - tree clusters from hcluster tree with distance<dist
    clusters = {}
    if clust.distance<dist:
        # we have found a cluster subtree
        return [clust] 
    else:
        # check the right and left branches
        cl = []
        cr = []
        if clust.left != None: 
            cl = extract_clusters(clust.left, dist = dist)
        if clust.right != None: 
            cr = extract_clusters(clust.right, dist = dist)
        return cl + cr 

def get_cluster_elements(clust):
    # return ids for elements in a cluster sub - tree
    if clust.id>0:
        # positive id means that this is a leaf
        return [clust.id]
    else:
        # check the right and left branches
        cl = []
        cr = []
        if clust.left != None: 
            cl = get_cluster_elements(clust.left)
        if clust.right != None: 
            cr = get_cluster_elements(clust.right)
        return cl + cr


def printclust(clust, labels = None, n = 0):
    # indent to make a hierarchy layout
    for i in range(n): print ' ', 
    if clust.id<0:
        # negative id means that this is branch
        print ' - '
    else:
        # positive id means that this is an endpoint
        if labels == None: print clust.id
        else: print labels[clust.id]

    # now print the right and left branches
    if clust.left != None: printclust(clust.left, labels = labels, n = n + 1)
    if clust.right != None: printclust(clust.right, labels = labels, n = n + 1)



def getheight(clust):
    # Is this an endpoint? Then the height is just 1
    if clust.left == None and clust.right == None: return 1

    # Otherwise the height is the same of the heights of
    # each branch
    return getheight(clust.left) + getheight(clust.right)

def getdepth(clust):
    # The distance of an endpoint is 0.0
    if clust.left == None and clust.right == None: return 0

    # The distance of a branch is the greater of its two sides
    # plus its own distance
    return max(getdepth(clust.left), getdepth(clust.right)) + clust.distance



def drawdendrogram(clust, image_list, sample_list, dendrogram_out = 'clusters.png', map = None):
    # height and width
    h = getheight(clust)*180 + 100
    w = 900
    depth = getdepth(clust)

    # width is fixed, so scale distances accordingly
    if(depth == 0):
        scaling = 1
    else:
        scaling = float(w - 150)/depth

    # Create a new image with a white background
    if map:
        img = Image.new('RGB', (w + 250, h), (255, 255, 255))
    else:
        img = Image.new('RGB', (w + 100, h), (255, 255, 255))

    draw = ImageDraw.Draw(img)
    draw.line((0, h/2, 10, h/2), fill = (0, 0, 0), width = 3)

    # Draw the first node
    drawnode(draw, clust, 10, (h/2), scaling, image_list, sample_list, img, map = map)
    img.save(dendrogram_out)

def drawnode(draw, clust, x, y, scaling, image_list, sample_list, img, map = None):
    if clust.id<0:
        h1 = getheight(clust.left)*180
        h2 = getheight(clust.right)*180
        top = y - (h1 + h2)/2
        bottom = y + (h1 + h2)/2
        # Line length
        ll = clust.distance*scaling
        # Vertical line from this cluster to children
        draw.line((x, top + h1/2, x, bottom - h2/2), fill = (0, 0, 0))

        # Horizontal line to left item
        draw.line((x, top + h1/2, x + ll, top + h1/2), fill = (0, 0, 0), width = 3)

        # Horizontal line to right item
        draw.line((x, bottom - h2/2, x + ll, bottom - h2/2), fill = (0, 0, 0), width = 3)

        # Call the function to draw the left and right nodes
        drawnode(draw, clust.left, x + ll, top + h1/2, scaling, image_list, sample_list, img, map = map)
        drawnode(draw, clust.right, x + ll, bottom - h2/2, scaling, image_list, sample_list, img, map = map)
    else:
        # If this is an endpoint, draw a thumbnail image
        nodeim = Image.open(image_list[clust.id])
        nodeim.thumbnail((300, 300))
        ns = nodeim.size

        fi = int(x + 0.1)
        se = int((y - ns[1]//2) + 0.1)
        th = int(x + ns[0] + 0.1)
        fo = int((y + ns[1] - ns[1]//2) + 0.1)

        #print (x, y - ns[1]//2, x + ns[0], y + ns[1] - ns[1]//2), img.size
        try:
            img.paste(nodeim, (fi, se, th, fo))
        except:
            print "sic"
            print (fi, se, th, fo)

        if map:
            for group in map["sample_groups"]:
                if sample_list[clust.id] in map["sample_groups"][group]:
                    break

            draw = ImageDraw.Draw(img)
            draw.line((th, (se + fo)/2.0, 1050, (se + fo)/2.0), fill = "#DDD", width = 4)
            draw.rectangle((1050, se, 1100, fo), fill=map["group_colors"][group], outline="#DDD")

def m(tree):
    """just get the list of ids"""
    if tree.id < 0:
        m(tree.left)
        m(tree.right)
        return
    else:
        print tree.id, tree.vec
        return


def generate(samples_dict, otu_library, pie_charts_dir = "", dendrogram_prefix = "", ranks = None, save_dir = None, map = None):
    """
    Generates piechart dendrograms for the given dict of samples. if save_dir is None, this function will save files in pie_charts_dir
    """
    piecharts = os.path.join(pie_charts_dir, "mini_piechart_%s_%s.png")

    if ranks:
        ranks = ranks
    else:
        ranks = framework.constants.ranks['rdp']

    for rank in ranks:
        samples, components, features = generate_feature_vectors_from_samples_dict(samples_dict, otu_library, rank = rank)

        img_list = []
        sample_list = []
        for sample in samples:
            img_list.append(piecharts % (rank, sample))
            sample_list.append(sample)

        clust = hcluster(features)

        if save_dir:
            drawdendrogram(clust, img_list, sample_list, dendrogram_out = os.path.join(save_dir, dendrogram_prefix + rank + ".png"), map = map)
        else:
            drawdendrogram(clust, img_list, sample_list, dendrogram_out = os.path.join(pie_charts_dir, dendrogram_prefix + rank + ".png"), map = map)


if __name__  ==  "__main__":
    import rdp
    samples_dict = rdp.read_samples_dictionary("/home/amanda/repo/ferris/framework/analyses/f62c0136a808f674c037df10c436da5543b62851/samples_dict_serialized")
    otu_library = rdp.read_samples_dictionary("/home/amanda/repo/ferris/framework/analyses/f62c0136a808f674c037df10c436da5543b62851/otu_library")
    pie_charts_dir = "/home/amanda/repo/ferris/framework/analyses/f62c0136a808f674c037df10c436da5543b62851/piecharts/"
    map = {'name': 'squirrel', 'heatmaps': {'phylum': u'f62c0136a808f674c037df10c436da5543b62851/maps/4/heatmaps/abundance_heatmap_phylum.png', 'genus': u'f62c0136a808f674c037df10c436da5543b62851/maps/4/heatmaps/abundance_heatmap_genus.png', 'order': u'f62c0136a808f674c037df10c436da5543b62851/maps/4/heatmaps/abundance_heatmap_order.png', 'family': u'f62c0136a808f674c037df10c436da5543b62851/maps/4/heatmaps/abundance_heatmap_family.png', 'class': u'f62c0136a808f674c037df10c436da5543b62851/maps/4/heatmaps/abundance_heatmap_class.png'}, 'ranks': ['genus', 'family', 'order', 'class', 'phylum'], 'sample_groups': {'b': ['S6', 'S7', 'S8', 'S9'], 't': ['S1', 'S2', 'S3', 'S4', 'S5']}, 'instance': u'4', 'group_colors': {'b': '#9ACD32', 't': '#4169E1'}, 'excluded': [], 'included': ['S1', 'S2', 'S3', 'S4', 'S5', 'S6', 'S7', 'S8', 'S9'], 'percent_abundance_files': {'phylum': u'f62c0136a808f674c037df10c436da5543b62851/maps/4/percent_abundance_phylum', 'genus': u'f62c0136a808f674c037df10c436da5543b62851/maps/4/percent_abundance_genus', 'order': u'f62c0136a808f674c037df10c436da5543b62851/maps/4/percent_abundance_order', 'family': u'f62c0136a808f674c037df10c436da5543b62851/maps/4/percent_abundance_family', 'class': u'f62c0136a808f674c037df10c436da5543b62851/maps/4/percent_abundance_class'}, 'taxon_charts_dir': u'f62c0136a808f674c037df10c436da5543b62851/maps/4/taxon_charts'}
    generate(samples_dict, otu_library, pie_charts_dir, ranks = ["genus"], save_dir = "./", map = map)




