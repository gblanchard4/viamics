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
#A set of useful functions for using makeblastdb and blastn from python. These were written for the expected purpose
#of using makeblastdb to format fasta files, and then using blastn against the created blast DBs to classify 16s
#rRNA sequences obtained from pyroseqencing.
#
import itertools
import sys
import os
import shlex
import subprocess
from framework import constants as c
import framework.tools.helper_functions as helper_functions
from framework.tools.helper_functions import SerializeToFile, DeserializeFromFile

sys.path.append('../..')

blastn_cmd = "blastn -query %(fasta)s -outfmt %(fmt)d -num_alignments %(num)d -db %(blast_db)s -out %(blast_out)s -num_threads "+ str(c.blast_number_of_threads)
#makeblastdb_cmd = "makeblastdb -in %(in)s -dbtype nucl -out %(out)s -title %(name)s -input_type %(input_type)s"
makeblastdb_cmd = "makeblastdb -in %(in)s -dbtype nucl -out %(out)s "

def run_blastn(sequences_path,blast_output_path,blast_db_path,fmt=7,num=5,error_log='/tmp/error_log'):
    """Runs blastn on the fasta file at sequences_path against the db at blast_db_path. Blocks until blast is finished. The blastn executable is assumed to be on the path.
    May choke on filenames with spaces in them."""

    #import pdb; pdb.set_trace()
    command = (blastn_cmd % {'fasta':sequences_path, 'blast_out':blast_output_path, 'blast_db':blast_db_path,'fmt':fmt, 'num':num})
    #print command
    args = shlex.split(str(command))
    try:
        ret_val = subprocess.call(args, stderr=open(error_log,'w'))
    except OSError:
        raise OSError('Error occurred trying to run BLAST. Is blastn on the path?')
    except TypeError as e:
        raise e
    return (ret_val, error_log)

def make_blastdb(fasta_path, name,output_dir="",error_log=None,input_type="fasta"):
    """runs makeblastdb (executable must be on path) to package the file at input_file into a BLAST DB. May choke on filenames with spaces in them """
    #error_log = os.path.join(c.blastdb_dir,name,c.blast_error_name)
    if error_log:
        error_log = open(error_log,'w')
    out = os.path.join(output_dir,name)
    args = shlex.split(str(makeblastdb_cmd))
    varargs = {"in":fasta_path, "out":out, "name":name,'input_type':input_type}
    args =  [str(a % varargs) for a in args] 
    print "\n\nrunning "+str(args)
    
    exit_val = subprocess.call(args)
    return exit_val

class Blast_Result:
    """A collection of alignments for an individual query sequence. Currently supports blastn output in format 6 and 7 """

    def __init__(self, output, fmt=7):
        """BlastResult(output, fmt=7) where output is a string containing the tabular BLAST results which all pertain to a particular query sequence
        self.alignments is a list of Alignment objects."""
        
        if fmt != 7 and fmt != 6:
            raise ValueError('Blast format %d is not supported yet' % fmt)
        output = [line.split('\t') for line in
                  filter(lambda l: not l.startswith('#'),output.strip().split('\n'))]
        for l in output:
            assert l[0] == output[0][0]
        self.id = output[0][0]
        self.alignments = [Alignment(l,fmt=fmt) for l in output]

class Alignment:
    """A single alignment for an individual query sequence. Currently supports blastn output in format 6 and 7
    fields (all from blast output, see NCBI blast docs for more information):
        qseqid	Query sequence ID
        sseqid	search (Matched) sequence ID
        pident	Percent identity between query and search sequence
        length	Length of alignment
        mismatch
        gapopen
        qstart
        qend
        sstart
        send
        evalue	Probability of such an alignment occurring by chance
        bitscore
"""

    def __init__(self, output, fmt=7):
        if fmt != 7 and fmt != 6:
            raise ValueError('Blast format %d is not supported yet' % fmt)
        fields = ['qseqid', 'sseqid', 'pident', 'length', 'mismatch', 'gapopen', 'qstart', 'qend', 'sstart', 'send', 'evalue', 'bitscore']
        try:
            vals = output.strip().split('\t')
        except AttributeError:#not a string, maybe it's iterable
            vals = output
        if len(fields) != len(vals):
            raise ValueError('Blast output format appears to be incorrect: %s' % str(vals))
        for field,val in zip(fields, vals):
            setattr(self, field, val)
        
def blast_results(f, fmt=7):
    """f is a file-like object that contains the output of a blastn search. Returns an iterator of BlastResult objects. """
    if fmt != 7 and fmt != 6:
            raise ValueError('Blast format %d is not supported yet' % fmt)
    id = ""
    result = ""
    #import pdb; pdb.set_trace()
    for line in f:
        if not (line.startswith('#') or line.strip() == ''):
            line_id = line.strip().split('\t')[0]
            if not (line_id == id):
                id = line_id
                if not result == '':
                    #print 'result: '+result
                    yield Blast_Result(result)
                    result = ""
            
            result += line
    if result.strip() != '':
        yield Blast_Result(result)#lazy fix to catch last result
            
def create_samples_dictionary(blast_output_path, legend_path, separator):
    """reads output file and and creates total count entries in the dictionary for matching samples in the 'samples' list. This is the fundamental operation that a module needs to do - the commons module assumes that a samples_dict has already been created for any analysis.

    samples_dict contains the {sample_id:{level:{otu_id:count,...},...},...} information used for the various visual and statistical analyses"""
    samples = {}
    #import pdb; pdb.set_trace()
    legend = DeserializeFromFile(legend_path)
    ranks = legend['ranks']
    blast = blast_results(open(blast_output_path))
    
    for result in blast:#iterate over blast results for each query seq
        a = best_alignment(result)
        sample, sequence = a.qseqid.split(separator)
        if sample not in samples:
            samples[sample] = dict(zip(ranks, iter(dict,0)))
        #get the name of matched sequence from the legend, if possible
        try:
            taxa = legend[a.sseqid]
            assert len(taxa) == len(ranks)
        except KeyError:#otherwise just name it after the query seq
            taxa = itertools.repeat(a.sseqid)
            
        for rank, taxon in zip(ranks, taxa):#Increment each otu given by the legend
            try:
                samples[sample][rank][taxon] += 1
            except KeyError:
                samples[sample][rank][taxon] = 1
    
    for sample in samples:#compute total reads for each sample
        samples[sample]['tr'] = sum(samples[sample][ranks[0]].values())

    return samples


def get_otu_library(blast_output_path, legend_path, separator):
    lib = []
    legend = DeserializeFromFile(legend_path)
    ranks = legend['ranks']
    blast = blast_results(open(blast_output_path))
    already_added = set()

    for result in blast:
        a = best_alignment(result)
        sample, sequence = a.qseqid.split(separator)
        
        try:
            taxa = legend[a.sseqid]
            assert len(taxa) == len(ranks)
        except KeyError:#otherwise just name it after the query seq
            taxa = list(itertools.islice(itertools.repeat(a.sseqid), len(ranks)))
        if taxa[len(taxa)-1] not in already_added:
            lib.append(taxa)
            already_added.add(taxa[len(taxa)-1])

    lib.sort()
    
    return lib


def best_alignment(result):
    return max(result.alignments, key=lambda e: e.pident)


def general_confidence_analysis(blast_results, save_path):
    """parses BLAST output to create a plot of e-value and bit-score for each alignment

    UNDER CONSTRUCTION"""


    #create a list of tuples of (max_bitscore, min_evalue) from all the alignments of each result
    def f(res):#rename. only used here
        a = best_alignment(res)
        return (float(a.bitscore), float(a.evalue))
    scores_and_e_vals = map(f, blast_results)
    


    def maxes(pairs):
        a,b = 0,0
        for t in pairs:
            a = t[0] if t[0] > a else a
            b = t[1] if t[1] > b else b
        return (a,b)
    max_vals = maxes(scores_and_e_vals)

    #TEMPORARY HACK:
    ################################################################################
    max_val = max_vals[1]
    max_val = max_val + max_val * 10 / 100
    m = ['E-value']
    group_colors = {'E-value':'#2222FF'}
    plot_dict = {'E-value':[i[1] for i in scores_and_e_vals]}
    ################################################################################
    

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
