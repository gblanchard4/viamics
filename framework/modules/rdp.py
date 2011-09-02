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
# Module functions for 16S rRNA sequence analyses with RDP.
#

import os

import framework.tools.rdp

from framework import constants as c
from framework.tools import helper_functions
from framework.tools import fasta

from framework.tools.logger import debug
from framework.tools.helper_functions import DeserializeFromFile, SerializeToFile, GetCopy

def _preprocess(p, request_dict):
    #fasta.stripped specifies an open keyfile object, but all it does is
    #"for line in keys" so a list of strings works here. Using a list avoids all
    #the nonsense of sending another file from the client.
    mode = request_dict.get("qa_mode")
    
    return fasta.fasta_qa_preprocess(
        mode,
        request_dict.get("data_file_path"),
        request_dict.get("codes_primers"),#keyfile. see above
        chimeras = request_dict.get("chim"),
        homopolymer_length = request_dict.get("homopolymer_length"))
                                     
    
def _exec(p, request_dict):
    """execute a pristine analysis with"""

    p.set_analysis_type("rdp")
    p.threshold = request_dict.get('threshold')

    seperator = request_dict['seperator']
    debug("storing seperator: '%s'" % seperator, p.files.log_file)
    open(p.files.seperator_file_path, 'w').write(seperator)

    if p.threshold:
        debug("storing confidence threshold", p.files.log_file)
        with open(p.files.threshold_path,'w') as f:
            f.write(str(p.threshold))

    debug("Extracting QA info", p.files.log_file)
    cmt = open(p.files.data_comment_file_path,'w')
    for line in open(p.files.data_file_path):
        if line.startswith(';'):
            cmt.write(line)
    cmt.close()
            
    #running rdp on data
    number_of_sequences = helper_functions.get_number_of_lines(p.files.data_file_path) / 2
    debug("running rdp on %d sequences" % number_of_sequences, p.files.log_file)
    framework.tools.rdp.run_classifier(c.rdp_running_path, p.files.data_file_path, p.files.rdp_output_file_path, p.files.rdp_error_log_file_path)

    samples_dictionary(p)
    rdp_general_confidence_image(p)
    rdp_otu_confidence_analysis(p)
    rdp_samples_confidence_image(p)
    otu_library(p)
    rarefaction_curves(p)
    if hasattr(p,'threshold'):
        separate_low_confidence(p)


def _append(p, request_dict):
    # TODO: there should be one function in RDP that takes care of all these in one step.
    # actually that one step solution should exist in every module that creates samples_dict eventually.
    # so the mess here for new analyses and additional samples could be carried into their own modules.
    # without putting everything together nicely in modules with standard hooks in them, there is no way to
    # fix this mess.

    p.threshold = request_dict.get('threshold')

    if p.threshold:
        debug("storing confidence threshold", p.files.log_file)
        with open(p.files.threshold_path,'w') as f:
            f.write(str(p.threshold))

    debug("Extracting unique sample names from additional FASTA file", p.files.log_file)
    additional_data_file_path = request_dict['additional_data_file_path']
    seperator = open(p.files.seperator_file_path).read()

    additional_samples = framework.tools.helper_functions.sorted_copy(framework.tools.rdp.extract_sample_names(additional_data_file_path, seperator))
    original_samples = framework.tools.helper_functions.sorted_copy([sample.strip() for sample in open(p.files.all_unique_samples_file_path).readlines()])

    number_of_sequences = sum(1 for l in open(additional_data_file_path) if l.startswith('>'))

    additional_rdp_output_path = os.path.join(p.dirs.analysis_dir, "additional_rdp_output")
    debug("Running rdp on %d additional sequences" % number_of_sequences, p.files.log_file)
    framework.tools.rdp.run_classifier(c.rdp_running_path, additional_data_file_path, additional_rdp_output_path, p.files.rdp_error_log_file_path)

    if p.threshold:
        debug("Separating low confidence sequences", p.files.log_file)
        lo_seqs = framework.tools.rdp.low_confidence_seqs(open(additional_data_file_path),
                                                          open(additional_rdp_output_path),
                                                          p.threshold,
                                                          seperator)
        o = open(p.files.low_confidence_seqs_path,'a')
        for s in lo_seqs:
            o.write(s)
        o.close()

    #import pdb; pdb.set_trace()
    debug("Merging additional data with the original RDP results", p.files.log_file)
    framework.tools.rdp.merge(p.files.samples_serialized_file_path, additional_samples, original_samples, additional_rdp_output_path, p.files.rdp_output_file_path, seperator)

    debug("Reading updated samples dict", p.files.log_file)
    samples_dict = DeserializeFromFile(p.files.samples_serialized_file_path)

    debug("Unique samples in samples dict being stored in samples file", p.files.log_file)
    samples = framework.tools.helper_functions.sorted_copy(samples_dict.keys())
    open(p.files.all_unique_samples_file_path, 'w').write('\n'.join(samples) + '\n')

    rdp_general_confidence_image(p)
    rdp_otu_confidence_analysis(p)
    rdp_samples_confidence_image(p)
    otu_library(p)
    os.remove(additional_rdp_output_path)


def _module_functions(p, request_dict):
    return {
        'rdp_01': {'func': samples_dictionary, 'desc': 'Samples dictionary'},
        'rdp_02': {'func': rdp_general_confidence_image, 'desc': 'RDP general confidence image'},
        'rdp_03': {'func': rdp_otu_confidence_analysis, 'desc': 'RDP OTU confidence image'},
        'rdp_04': {'func': rdp_samples_confidence_image, 'desc': 'RDP samples confidence image'},
        'rdp_05': {'func': rarefaction_curves, 'desc': 'Rarefaction curves'},
        'rdp_06': {'func': otu_library, 'desc': 'OTU library'},
        'rdp_07': {'func': separate_low_confidence, 'desc': "Separate low confidence sequences"}
    }

def _sample_map_functions(p, request_dict):
    return {}

#######################################
# module function definitions
#######################################

def samples_dictionary(p):
    debug("Computing samples dictionary", p.files.log_file)
    seperator = open(p.files.seperator_file_path).read()
    thresh = p.threshold if hasattr(p,'threshold') else None

    # read samples from RDP since it may have been updated.
    samples = list(set([sample.split(seperator)[0] for sample in open(p.files.rdp_output_file_path).readlines()]))
    open(p.files.all_unique_samples_file_path, 'w').write('\n'.join(samples) + '\n')
    samples_dict = framework.tools.rdp.create_samples_dictionary(p.files.rdp_output_file_path, seperator, samples,threshold=thresh)
    debug("Serializing samples dictionary object", p.files.log_file)
    SerializeToFile(samples_dict, p.files.samples_serialized_file_path)

def rdp_general_confidence_image(p):
    debug("Generating RDP Confidence figure", p.files.log_file)
    framework.tools.rdp.general_confidence_analysis(p.files.rdp_output_file_path, p.dirs.analysis_dir)

def rdp_otu_confidence_analysis(p):
    debug("Generating RDP confidence per otu figures", p.files.log_file)
    samples_dict = DeserializeFromFile(p.files.samples_serialized_file_path)
    samples = framework.tools.helper_functions.sorted_copy(samples_dict.keys())
    seperator = open(p.files.seperator_file_path).read()
    framework.tools.rdp.otu_confidence_analysis(p.files.rdp_output_file_path, p.dirs.type_specific_data_dir, seperator, samples)


def rdp_samples_confidence_image(p):
    debug("Refreshing RDP Confidence per sample figure", p.files.log_file)
    samples_dict = DeserializeFromFile(p.files.samples_serialized_file_path)
    seperator = open(p.files.seperator_file_path).read()
    samples = framework.tools.helper_functions.sorted_copy(samples_dict.keys())
    framework.tools.rdp.sample_confidence_analysis(p.files.rdp_output_file_path, p.dirs.analysis_dir, seperator, samples)


def otu_library(p):
    debug("Generating OTU Library", p.files.log_file)
    otu_library = framework.tools.rdp.get_otu_library(p.files.rdp_output_file_path)
    SerializeToFile(otu_library, p.files.otu_library_file_path)

def rarefaction_curves(p):
    samples_dict = DeserializeFromFile(p.files.samples_serialized_file_path)
    folds = c.number_of_folds_for_rarefaction_curves
    debug("Re-generating rarefaction curves: computing rarefraction dict (%d folds)" % folds, p.files.log_file)
    rarefaction_dict = framework.tools.rarefaction.generate_dict(samples_dict, number_of_folds = folds)
    debug("Re-generating rarefaction curves: saving rarefaction dict", p.files.log_file)
    SerializeToFile(rarefaction_dict, p.files.rarefaction_dict_serialized_file_path)
    debug("Re-generating rarefaction curves: generating all samples image", p.files.log_file)
    framework.tools.rarefaction.generate_all_samples_figure(rarefaction_dict, save_path = p.files.rarefaction_curves_all_samples_file_path)
    debug("Re-generating rarefaction curves: generating individual images", p.files.log_file)
    framework.tools.rarefaction.generate_individual_figures(rarefaction_dict, save_path = p.dirs.rarefaction_curves_dir, prefix = c.rarefaction_curve_file_prefix)
    debug("Re-generating rarefaction curves: Done", p.files.log_file)

def separate_low_confidence(p):
    debug("Separating low confidence sequences", p.files.log_file)
    separator = open(p.files.seperator_file_path).read()    
    lo_seqs = framework.tools.rdp.low_confidence_seqs(open(p.files.data_file_path),
                                                      open(p.files.rdp_output_file_path),
                                                      p.threshold,
                                                      separator)
    o = open(p.files.low_confidence_seqs_path,'w')
    for s in lo_seqs:
        o.write(s)
    o.close()

