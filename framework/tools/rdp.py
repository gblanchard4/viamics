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
################################################################################
#RDP stuff.
#
#Tools for analysing a FASTA file using the RDP classifier
#
#An assumption throughout this module (and all of viamics) is that the ids of
#FASTA sequences are composed of a sample id, which labels a group of sequences,
#and a unique sequence id. These are located directly after the '>', and are
#separated by a variable separator character.
################################################################################
# example run:
#
# python rdp_classifier_run.py -f BV/ferris92Labeled.fas -o RDP_output_of_all_BV.txt -s '_' -r RDP_Classifier/rdp_classifier_2.1/ -p ABUNDANCE
#


import os
import sys
import shlex
import shutil
import cPickle
import subprocess
from itertools import izip
import random as r

from framework import constants as c
import pylab
from optparse import OptionParser

sys.path.append("../../")
from framework.tools import helper_functions

#I want to have 'domain' in RDPResult.classifications, but adding it to
#c.ranks['rdp'] breaks other things in the web client. hence:
ALL_RANKS = ['domain', 'phylum', 'class', 'order', 'family', 'genus']


"""MZH-92_F58614Y04IOLGX\t\t\t\t\tBacteria\tdomain\t1.0\t"Fusobacteria"\tphylum\t1.0\t"Fusobacteria"\tclass\t1.0\t"Fusobacteriales"\torder\t1.0\t"Leptotrichiaceae"\tfamily\t1.0\tSneathia\tgenus\t1.0\n"""#breaks constructor

class RDPResult:
    """    The constructor for this class takes a single line from the RDP output in  'fixrank' format, from which it can read the taxonomic information.

    If the constructor is given a kwarg 'separator', the ID of the sequence will be split into sample id and sequence id, assuming the ID looks like 'sample_id<separator>sequence_id. If there is no separator, both sample_id and sequence_id will be the entire id'

Properties:
    sample_id: The sample (group of sequences) that this sequence comes from.

    sequence_id: a unique ID for this sequence.

    classifications: a dict with keys ['phylum','class','order','family','genus'] and values are the classification of the sequence for that level.

    confidences: a dict with the same keys as classifications, and values are the classification confidences returned by RDP"""

    def __init__(self, outfile_line,separator=None):
        #import pdb;pdb.set_trace()
        self.data = outfile_line
        outfile_line = outfile_line.split('\t')
        ids = filter(lambda i: i != '',outfile_line[0].split(separator))
        if separator and len(ids):
            self.sample_id = ids[0]
            self.seq_id = '_'.join(ids[1:])
        else:
            #wasn't given a separator or one id is missing, hopefully this means client is not using id
            self.sample_id = self.seq_id = outfile_line[0]
        rank_indices = [5,8,11,14,17,20]
        taxonomic_ranks = [outfile_line[i] for i in rank_indices]
        confidences = [outfile_line[i+2] for i in rank_indices]
        for i,conf in enumerate(confidences):
            try:
                confidences[i] = float(conf)
            except ValueError:
                confidences[i] = conf.strip()
        ranks = ALL_RANKS#not using c.ranks['rdp'] b/c it does not include domain. Changing it breaks other things
        self.classifications = dict(zip(ranks,taxonomic_ranks))
        self.confidences = dict(zip(ranks, confidences))
        filled = filled_ranks(self.classifications)
        self.taxonomy_string = str.join(';',(filled[r] for r in ranks))

        

def rdp_results(rdp_file,separator):
    for line in rdp_file:
        yield RDPResult(line,separator)

def low_confidence_seqs(fasta_file, rdp_outfile, threshold, separator):
    """Sequences which the classifier marked as below the given threshold. The sequence IDs in the fasta file must be a superset of those in the RDP output. The expected case is that RDP was run against the fasta file to generate the output """
    #first assume the rdp out and fasta line up exactly:
    results = rdp_results(rdp_outfile,separator)
    sequences = helper_functions.seqs(fasta_file)
    below_threshold = set(res.seq_id for res in results if float(res.confidences['genus']) < threshold)
    for seq in sequences:
        ids = filter(lambda i: i.strip() != '',seq.split()[0].split(separator))
        s_id = ids[1]
        if s_id in below_threshold:
            yield seq
        
    


# command to run RDP classifier
cmd = "java -Xmx1g -jar rdp_classifier-2.2.jar -q %(fasta_file)s -o %(rdp_output_file)s -f fixrank &> %(error_log)s"

def run_classifier(rdp_running_path, fasta_file, rdp_output_file, error_log = '/tmp/error_log'):
    """changes directory, runs RDP, returns back to the original directory"""
    cur_dir = os.getcwd()
    os.chdir(rdp_running_path)
    #uses subprocess.call instead of older os.system.
    #subprocess was added in python 2.4, if backwards compat is an issue
    #we can add a condition to check the version. may need to do other stuff 
    #too as os.system was seeming to not block in some cases.
    command = (cmd % {'fasta_file': fasta_file, 'rdp_output_file': rdp_output_file, 'error_log': error_log})
    args = shlex.split(command)
    ret_val = subprocess.call(args)
    #ret_val = os.system(cmd % {'fasta_file': fasta_file, 'rdp_output_file': rdp_output_file, 'error_log': error_log})
    os.chdir(cur_dir)
    return (ret_val, error_log)

def merge(samples_serialized_file_path, additional_samples, original_samples, additional_rdp_output_file, original_rdp_output_file, seperator):
    samples_in_original_rdp_output = list(set([s.split(seperator)[0] for s in open(original_rdp_output_file).readlines()]))
    print "samples in rdp output:", samples_in_original_rdp_output
    print "samples in fasta:", original_samples
    print "additional samples:", additional_samples

    original_samples = list(set(original_samples + samples_in_original_rdp_output))

    print "final original samples: ", original_samples


    samples_to_replace = []
    for sample in additional_samples:
        if sample in original_samples:
            samples_to_replace.append(sample)

    print "to replace:", samples_to_replace

    if len(samples_to_replace):
        original_rdp_output_lines = open(original_rdp_output_file).readlines()
        temporary_rdp_output_file = original_rdp_output_file + '.tmp'
        temporary_rdp_output_file_obj = open(temporary_rdp_output_file, 'w')

        # tmp_rdp_output += (original samples) - (samples to replace)
        i = 0
        while i < len(original_rdp_output_lines):
            sample = original_rdp_output_lines[i].split(seperator)[0]
            if sample in samples_to_replace:
                i += 1
            else:
                temporary_rdp_output_file_obj.write(original_rdp_output_lines[i])
                i += 1

        temporary_rdp_output_file_obj.write(additional_rdp_output_file.read())

        temporary_rdp_output_file_obj.close()
        shutil.move(temporary_rdp_output_file, original_rdp_output_file)

    else:
        rdp_output_file_obj = open(original_rdp_output_file, 'a')
        for line in open(additional_rdp_output_file).readlines():
            rdp_output_file_obj.write(line)
        rdp_output_file_obj.close()

        # this could be used to update FASTA file
        #i = 0
        #while i < len(original_rdp_output_lines):
        #    if original_rdp_output_lines[i].startswith('>'):
        #        sample = original_rdp_output_lines[i].split(seperator)[0][1:]
        #        if sample in samples_to_replace:
        #            i += 1
        #            while True:
        #                if original_rdp_output_lines[i].startswith('>'):
        #                    break
        #                else:
        #                    i += 1
        #        else:
        #            temporary_rdp_output_file_obj.write(original_rdp_output_lines[i])
        #            i += 1
        #    else:
        #        temporary_rdp_output_file_obj.write(original_rdp_output_lines[i])
        #        i += 1

    all_samples = list(set(original_samples + additional_samples))
    updated_samples_dict = create_samples_dictionary(original_rdp_output_file, seperator, all_samples)
    write_samples_dictionary(samples_serialized_file_path, updated_samples_dict)


def write_samples_dictionary(serialized_object_file, samples_dict):
    """serializes samples_dict into 'options.serialized_object_file'"""
    return cPickle.dump(samples_dict, open(serialized_object_file, 'w'))

def read_samples_dictionary(serialized_object_file):
    """reads the dict stored in 'options.serialized_object_file'"""
    return cPickle.load(open(serialized_object_file))

def get_otu_library(rdp_output_file):
    """returns a unique list of OTUs that were found in the library"""
    
    taxonomic_ranks = ['domain', 'phylum', 'class', 'order', 'family', 'genus']

    genuses = []
    otu_library = []

    for result in rdp_results(open(rdp_output_file),separator=None):#don't care about separator b/c id does not matter at this stage
        #sometimes taxonomic names are empty! gotta fix that!
        #TODO use filled_ranks instead of this
        last_non_empty_rank = ''

        for i in result.classifications.values():
            if i == "":
                i = "(%s)" % (last_non_empty_rank)
            else:
                last_non_empty_rank = i

        if result.classifications['genus'] not in genuses:
            genuses.append(result.classifications['genus'])
            otu_library.append([result.classifications[r] for r in taxonomic_ranks])

    otu_library.sort()

    return otu_library

def filled_ranks(classifications):
    result = {}
    ranks = ALL_RANKS
    last_filled = ''
    for r in ranks:
        result[r] = classifications[r] if classifications[r] != '' else "(%s)" % last_filled
        last_filled = result[r].strip('()')

    return result


def create_samples_dictionary(rdp_output_file, seperator, samples,threshold=None):
    """reads output file and and creates total count entries in the dictionary for matching samples in the 'samples' list. This is the fundamental operation that a module needs to do - the commons module assumes that a samples_dict has already been created for any analysis.

    samples_dict contains the {sample_id:{level:{otu_id:count,...},...},...} information used for the various visual and statistical analyses"""

    samples_dict = {}

    for res in rdp_results(open(rdp_output_file),seperator):
        if res.sample_id in samples:
            #line is from a sample we're interested in

            taxonomic_ranks = ['domain', 'phylum', 'class', 'order', 'family', 'genus']
            taxonomic_ranks = [(k,res.classifications[k]) for k in taxonomic_ranks]


            #sometimes taxonomic names are empty! gotta fix that!
            #TODO use filled_ranks instead of this
            last_non_empty_ranks = ['', '']
            for i in range(0, len(taxonomic_ranks)):
                if taxonomic_ranks[i][1] == "" or res.confidences[taxonomic_ranks[i][0]] < threshold:#all numbers are > None
                    taxonomic_ranks[i] = (taxonomic_ranks[i][0],"(%s: %s)" % (last_non_empty_ranks[0], last_non_empty_ranks[1]))
                else:
                    last_non_empty_ranks = taxonomic_ranks[i]
                    
            if samples_dict.has_key(res.sample_id):
                samples_dict[res.sample_id]['tr'] += 1
                for taxonomic_rank in taxonomic_ranks:
                    if samples_dict[res.sample_id][taxonomic_rank[0]].has_key(taxonomic_rank[1]):
                        samples_dict[res.sample_id][taxonomic_rank[0]][taxonomic_rank[1]] += 1
                    else:
                        samples_dict[res.sample_id][taxonomic_rank[0]][taxonomic_rank[1]] = 1
            else:
                samples_dict[res.sample_id] = {'tr': 1,
                                        'domain': {taxonomic_ranks[0][1]: 1},
                                        'phylum': {taxonomic_ranks[1][1]: 1},
                                        'class' : {taxonomic_ranks[2][1]: 1},
                                        'order' : {taxonomic_ranks[3][1]: 1},
                                        'family': {taxonomic_ranks[4][1]: 1},
                                        'genus' : {taxonomic_ranks[5][1]: 1}}

    return samples_dict


def otu_confidence_analysis(rdp_output_file, save_path, seperator, samples, rank = "genus"):
    otu_loc_in_rdp_output = {}
    # silly magic numbers.. one day I'll be very sorry for not storing them in one location.
    # please don't hate me; just consider fixing it :p
    otu_loc_in_rdp_output["genus"] = 20
    otu_loc_in_rdp_output["family"] = 17
    otu_loc_in_rdp_output["order"] = 14
    otu_loc_in_rdp_output["class"] = 11
    otu_loc_in_rdp_output["phylum"] = 8

    otu_loc = otu_loc_in_rdp_output[rank]

    otu_rdp_confidence_dict = {}

    lines = open(rdp_output_file).readlines()

    # fill the information into a dictionary with one pass.
    for line in lines:
        s = line.split('\t')
        sample = s[0].split(seperator)[0]
        otu = s[otu_loc]
        rdp_confidence = float(s[otu_loc + 2].strip())

        if not len(otu):
            continue

        if not sample in samples:
            continue

        if otu_rdp_confidence_dict.has_key(otu):
            if otu_rdp_confidence_dict[otu].has_key(sample):
                otu_rdp_confidence_dict[otu][sample].append(rdp_confidence)
            else:
                otu_rdp_confidence_dict[otu][sample] = [rdp_confidence]
        else:
            otu_rdp_confidence_dict[otu] = {}
            otu_rdp_confidence_dict[otu][sample] = [rdp_confidence]

    # now, fix the dict: if a sample doesn't have any sequences identified as a particular OTU,
    # lets put an empty list for that OTU in the dict. it will make things a little easier in
    # a second.
    for otu in otu_rdp_confidence_dict:
        for sample in samples:
            if not otu_rdp_confidence_dict[otu].has_key(sample):
                otu_rdp_confidence_dict[otu][sample] = [0]


    otu_rdp_confidence_tuples_list = [] # list of tuples: (otu_image_fname, otu_name, confidence_values_list)

    # now we're gonna create figures, and save them. also we'll use a semi-smart way to sort OTU's
    # to show them in a particular order.
    for otu in otu_rdp_confidence_dict:
        figure_file_name = rank + "_" + helper_functions.get_fs_compatible_name(otu) + '_rdp_confidence.png'
        total_number_of_sequences_for_otu = sum([sum(x) for x in otu_rdp_confidence_dict[otu].values()])
        otu_rdp_confidence_tuples_list.append((total_number_of_sequences_for_otu, otu, figure_file_name),)

        values_for_boxplots = []
        for sample in samples:
            values_for_boxplots.append(otu_rdp_confidence_dict[otu][sample])


        # we're ready to generate figures..
        max_val = 1.0

        max_val = max_val + max_val * 10 / 100

        width = len(samples) / 5
        if width < 5:
            width = 5

        if width > 15:
            width = 15

        fig = pylab.figure(figsize=(width, 4))

        pylab.rcParams['font.size'] = 8.0
        pylab.rcParams.update({'axes.linewidth' : 0, 'axes.axisbelow': False})
        pylab.rc('grid', color='0.50', linestyle='-', linewidth=0.1)
        pylab.grid(True)

        for i in range(0, len(samples)):
            b = pylab.boxplot(values_for_boxplots[i], positions=[i], sym=',', widths=0.3)
            pylab.setp(b['medians'], color='black')
            pylab.setp(b['whiskers'], color='black', alpha=0.9)
            pylab.setp(b['boxes'], color='black', alpha=0.9)
            pylab.setp(b['fliers'], color='black', alpha=0.9)
            pylab.setp(b['caps'], color='black', alpha=0.9)
            
            pylab.xlim(xmin=-0.75, xmax=len(samples) - 0.15)
            pylab.ylim(ymin=-max_val * 10 / 100, ymax=max_val)
            pylab.xticks(pylab.      arange(len(samples)), samples, rotation=90)

        if not save_path:
            pylab.show()
        else:
            pylab.savefig(os.path.join(save_path, figure_file_name))

        # clean memory
        try:
            fig.clf()
        except:
            pass
        pylab.close('all')

    otu_rdp_confidence_tuples_list.sort(reverse = True)

    if save_path:
    # get rid of the first entry -which was used for sorting- and store the ordering info
    # FIXME: could you please put data serializing and de-serializing function into the
    # helper_functions.py
        write_samples_dictionary(os.path.join(save_path, rank + "_rdp_confidence_ordering_info"), [(x[1], x[2]) for x in otu_rdp_confidence_tuples_list])


def general_confidence_analysis(rdp_output_file, save_path):
    """parses rdp output and stores classification confidence
       for every taxonomic level to generate an image"""

    lines = open(rdp_output_file).readlines()

    genus, family, order, clas, phylum = [], [], [], [], []

    for line in lines:
        s = line.split('\t')
        if s[22]:
            genus.append(float(s[22]))
        if s[19]:
            family.append(float(s[19]))
        if s[16]:
            order.append(float(s[16]))
        if s[13]:
            clas.append(float(s[13]))
        if s[10]:
            phylum.append(float(s[10]))

    plot_dict = {}
    plot_dict['genus'] = genus
    plot_dict['family'] = family
    plot_dict['order'] = order
    plot_dict['class'] = clas
    plot_dict['phylum'] = phylum

    group_colors = {
        'genus' : '#EDBEFE',
        'family': '#A9C5EB',
        'order' : '#8FFEDD',
        'class' : '#FFFF99',
        'phylum': '#FFCFA4',}


    m = ['genus', 'family', 'order','class', 'phylum']

    max_val = max([max(l) for l in plot_dict.values()])

    max_val = max_val + max_val * 10 / 100

    fig = pylab.figure(figsize=(8, 6))
    pylab.rcParams['font.size'] = 8.0
    pylab.rcParams.update({'axes.linewidth' : 0, 'axes.axisbelow': False})
    pylab.rc('grid', color='0.50', linestyle='-', linewidth=0.1)
    pylab.grid(True)
    
    for key in m:
        y_positions =  [((1 - (r.gauss(100, 3) /100)) + m.index(key)) for x in range(0, len(plot_dict[key]))]
        pylab.plot(y_positions, plot_dict[key], 'o', color = group_colors[key], ms = 8, mew = 0.4, alpha = .4)
        b = pylab.boxplot(plot_dict[key], positions=[m.index(key) + 0.35], sym=',', widths=0.2)
        pylab.setp(b['medians'], color=group_colors[key])
        pylab.setp(b['whiskers'], color='black', alpha=0.3)
        pylab.setp(b['boxes'], color='black', alpha=0.3)
        pylab.setp(b['fliers'], color='black', alpha=0.3)
        pylab.setp(b['caps'], color='black', alpha=0.3)
                
        pylab.xlim(xmin=-0.75, xmax=len(m) - 0.15)
        pylab.ylim(ymin=-max_val * 10 / 100, ymax=max_val)
        pylab.xticks(pylab.      arange(len(plot_dict)), m, rotation=90)

    if not save_path:
        pylab.show()
    else:
        pylab.savefig(os.path.join(save_path, "rdp_confidence.png"))

    # clean memory
    try:
        fig.clf()
    except:
        pass
    pylab.close('all')

def sample_confidence_analysis(rdp_output_file, save_path, seperator, samples_list = []):
    """parses rdp output and stores classification confidence
       for every sample at genus level to generate an image
       with box plots"""

    if not len(samples_list):
        return

    lines = open(rdp_output_file).readlines()

    confidence_dict = {}

    for line in lines:
        s = line.split('\t')
        sample = s[0].split(seperator)[0]
        genus_level_confidence = s[22]
        if sample in samples_list:
            if not confidence_dict.has_key(sample):
                confidence_dict[sample] = []
            confidence_dict[sample].append(float(genus_level_confidence.strip()))

    confidence_list = []

    for sample in samples_list:
        confidence_list.append(confidence_dict[sample])

    max_val = max([max(l) for l in confidence_list])

    max_val = max_val + max_val * 10 / 100

    width = len(samples_list) / 5
    if width < 5:
        width = 5

    if width > 15:
        width = 15

    fig = pylab.figure(figsize=(width, 4))

    pylab.rcParams['font.size'] = 8.0
    pylab.rcParams.update({'axes.linewidth' : 0, 'axes.axisbelow': False})
    pylab.rc('grid', color='0.50', linestyle='-', linewidth=0.1)
    pylab.grid(True)

    for i in range(0, len(samples_list)):
        b = pylab.boxplot(confidence_list[i], positions=[i], sym=',', widths=0.3)
        pylab.setp(b['medians'], color='black')
        pylab.setp(b['whiskers'], color='black', alpha=0.9)
        pylab.setp(b['boxes'], color='black', alpha=0.9)
        pylab.setp(b['fliers'], color='black', alpha=0.9)
        pylab.setp(b['caps'], color='black', alpha=0.9)

        pylab.xlim(xmin=-0.75, xmax=len(samples_list) - 0.15)
        pylab.ylim(ymin=-max_val * 10 / 100, ymax=max_val)
        pylab.xticks(pylab.      arange(len(samples_list)), samples_list, rotation=90)

    if not save_path:
        pylab.show()
    else:
        pylab.savefig(os.path.join(save_path, "rdp_confidence_per_sample.png"))

    # clean memory
    try:
        fig.clf()
    except:
        pass
    pylab.close('all')


def extract_sample_names(fasta_file, seperator):
    """finds unique sample names within the entire library, e.g., returns MZH-92 for MZH-92_F58614Y04I2TQV,
       MZH-92_F58614Y04I2TQV, MZH-92_F58614Y04IXSC2 and MZH-92_F58614Y04IKEJL"""
    return list(set([x[1:].split()[0].split(seperator)[0]
                     for x in open(fasta_file).readlines() if x[0] == ">"]))



################################################################################
#Command line usage:
################################################################################
def main(options, samples):
    error_val, error_log = run_classifier(options.rdp_running_path, options.fasta_file, options.rdp_output_file)
    # fix error handling..
    if int(error_val):
        print "something went wrong with RDP classificatoin. Error log is here: '%s'" % (error_log)
        sys.exit(3)
    #else: we have options.rdp_output_file ready.

    samples_dict = create_samples_dictionary(options.rdp_output_file, options.seperator, samples)

    if options.serialized_object_file:
        write_samples_dictionary(options.serialized_object_file, samples_dict)
    else:
        print samples_dict

    framework.tools.helper_functions.create_percent_abundance_file(samples_dict, output_file_path)

if __name__ == "__main__":
    parser = OptionParser()

    parser.add_option("-f", "--fasta-file", dest="fasta_file",
                              type="string", help="FASTA formatted input file with sequences", metavar="FILE")
    parser.add_option("-o", "--output-file", dest="rdp_output_file",
                              help="RDP classifier output", metavar="FILE")
    parser.add_option("-s", "--seperator", type="string", dest="seperator",
                              help="character that seperates sample name from unique sequenec id (e.g., '_' for 'MZH-92_F58614Y04I2TQV' where MZH-92 is the sample name and F58614Y04I2TQV is the unique sequence id in the FASTA library)")
    parser.add_option("-r", "--rdp-classifier-directory", type="string", dest="rdp_running_path",
                              help="full path to the directory where RDP classifier is on the file system")
    parser.add_option("-p", "--pickle-output-file", type="string", dest="serialized_object_file", metavar="FILE",
                              help="serialized object file for total abundance of bacteria in samples as a dictionary which could be imported an used by another Python program easily")

    (options, args) = parser.parse_args()

    if options.fasta_file == None:
        print "\nError: You need to provide an input file (FASTA library)\n"
        parser.print_help()
        sys.exit(1)
    elif not os.access(options.fasta_file, os.R_OK):
        print "\nError: Either '%s' is not a valid file name or you don't have permission to read it\n" % (options.fasta_file)
        parser.print_help()
        sys.exit(2)

    options.fasta_file = os.path.join(os.getcwd(), options.fasta_file)

    if options.rdp_output_file == None:
        print "\nError: You need to provide an output file name\n"
        parser.print_help()
        sys.exit(1)
    elif not os.access(os.path.dirname(options.rdp_output_file) or os.path.dirname("./"), os.W_OK):
        print "\nError: Either '%s' is not a valid path or you don't have permission to write there\n" % (options.rdp_output_file)
        parser.print_help()
        sys.exit(2)

    options.rdp_output_file = os.path.join(os.getcwd(), options.rdp_output_file)

    if not options.rdp_running_path:
        print "\nError: You need to provide RDP classifier source directory\n"
        parser.print_help()
        sys.exit(1)
    elif not os.access(options.rdp_running_path, os.R_OK):
        print "\nError: Either '%s' is not a valid directory or you don't have permission to read it\n" % (options.rdp_running_path)
        parser.print_help()
        sys.exit(2)


    if not options.seperator:
        print "\nError: You need to provide a 'seperator'\n"
        parser.print_help()
        sys.exit(1)

    samples = extract_sample_names(options.fasta_file, options.seperator)

    if len(samples) == 0:
        print "\nError: It seems either input file is not a FASTA file or 'seperator' is not correct\n"
        parser.print_help()
        sys.exit(1)

    main(options, samples)

