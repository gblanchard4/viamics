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
#Contains the process for running a viamics analysis using BLAST, using functions and classes from
#framework.tools.blast. This depends on blast databases being stored at constants.blastdb_dir, and having blastn
#blastn and makeblastdb executables on the path
#
#If the blastn or makeblastdb programs are throwing errors, one possible cause is spaces in the path to input
#or output files. I could not for the life of me figure this out (I think the blastn and makeblastdb programs just
#can't handle it), so I just stick underscores in the name the user gives. If Viamics is installed at say
#/home/username/Desktop/My bioinformatics folder/viamics, there could be a problem. 
import os
import cPickle

from framework.tools.helper_functions import SerializeToFile, DeserializeFromFile
from framework.tools.logger import debug
from framework.tools import fasta
import framework.constants as c
import framework.tools.blast
import framework.tools.helper_functions as helper_functions

def _preprocess(p, request_dict):
    #fasta.stripped specifies an open keyfile object, but all it does is
    #"for line in keys" so a list of strings works here. Using a list avoids all
    #the nonsense of sending another file from the client.
    mode = request_dict.get("qa_mode")
    try:
        return fasta.fasta_qa_preprocess(
            mode,
            request_dict.get("data_file_path"),
            request_dict.get("codes_primers"),#keyfile. see above
            homopolymer_length = request_dict.get("homopolymer_length"))
    except: 
        debug(helper_functions.formatExceptionInfo(), p.files.log_file)
        raise

def _exec(p, request_dict):
    p.set_analysis_type('blast')
    p.threshold = request_dict.get('threshold_dict') 

    
    separator = request_dict['seperator']#sic
    debug("storing separator: '%s'" % separator, p.files.log_file)
    open(p.files.seperator_file_path, 'w').write(separator)
    debug("storing DB name: '%s'" % request_dict['db_name'], p.files.log_file) 
    open(p.files.blast_db_name_path, 'w').write(request_dict['db_name'])
    if p.threshold:
        debug("storing confidence threshold", p.files.log_file) 
        with open(p.files.threshold_path,'w') as f:
            f.write(cPickle.dumps(p.threshold))

    
    
    #add length info to legend
    num_seqs = helper_functions.get_number_of_lines(p.files.data_file_path) / 2
    name = request_dict['db_name']
        #run blast on data
    blast_db = os.path.join(c.blastdb_dir,name,name)

    
    debug("Extracting QA info", p.files.log_file)
    cmt = open(p.files.data_comment_file_path,'w')
    for line in open(p.files.data_file_path):
        if line.startswith(';'):
            cmt.write(line)
    cmt.close()

    
    debug(("running blast on %d sequences against database: %s " % (num_seqs, request_dict['db_name'])), p.files.log_file)
    framework.tools.blast.run_blastn(p.files.data_file_path, p.files.blast_output_file_path, blast_db,num=1)


    
    
    samples_dictionary(p)
    samples = DeserializeFromFile(p.files.samples_serialized_file_path).keys()
    if len(samples) == 0:
        msg = 'error: samples dict contains no samples. perhaps no sequences in the query matched the datbase'
        debug(msg,p.files.log_file)
        raise ValueError(msg)
    else:
        open(p.files.all_unique_samples_file_path, 'w').write('\n'.join(samples) + '\n')
        debug("%d unique sample names stored" % len(samples), p.files.log_file)
        otu_library(p)
        if hasattr(p,'threshold'):
            separate_low_confidence(p)
    
    

def samples_dictionary(p):
    debug("Computing sample dictionary", p.files.log_file)
    db_name = open(p.files.blast_db_name_path).read()
    legend_path = os.path.join(c.blastdb_dir,
                               db_name,db_name+c.blast_legend_file_extension)
    samples_dict = framework.tools.blast.create_samples_dictionary(p.files.blast_output_file_path,
                                                                   legend_path,
                                                                   open(p.files.seperator_file_path).read(),
                                                                   thresholds=p.threshold)
    debug("Serializing samples dictionary object", p.files.log_file)
    SerializeToFile(samples_dict, p.files.samples_serialized_file_path)

def otu_library(p):
    debug("Generating OTU Library", p.files.log_file)
    db_name = open(p.files.blast_db_name_path).read()
    legend_path = os.path.join(c.blastdb_dir,
                               db_name,db_name+c.blast_legend_file_extension)
    otu_library = framework.tools.blast.get_otu_library(p.files.blast_output_file_path,
                                                        legend_path,
                                                        open(p.files.seperator_file_path).read())
    SerializeToFile(otu_library, p.files.otu_library_file_path)

def separate_low_confidence(p):
    debug("Separating low confidence sequences", p.files.log_file)
    separator = open(p.files.seperator_file_path).read()    
    lo_seqs = framework.tools.blast.low_confidence_seqs(open(p.files.data_file_path),
                                                      open(p.files.blast_output_file_path),
                                                      p.threshold,
                                                      separator)
    with open(p.files.low_confidence_seqs_path,'w') as o:
        for s in lo_seqs:
            o.write(s)


def _module_functions(p, request_dict):
    return {
        'blast': {'func': samples_dictionary, 'desc': 'Samples dictionary'},
        'blast': {'func': otu_library, 'desc': 'OTU library'}
    }

def _sample_map_functions(p, request_dict):
    return {}
