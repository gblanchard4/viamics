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

################################################################################
#FASTA module.
#Contains tools for general operations on FASTA files
################################################################################

import sys, os, re, time
import shlex, subprocess
from collections import deque

from framework.tools import helper_functions
from framework import constants
seqs = helper_functions.seqs

#QA mode constants. Specify mode by *bitwise* ORing them together,
#e.g. (STRIP_BARCODES_PRIMERS | STRIP_LIBERAL | REMOVE_CHIMERAS):
STRIP_BARCODES_PRIMERS     = 0b1000
STRIP_LIBERAL              = 0b0100
REMOVE_HOMOPOLYMERS        = 0b0010
REMOVE_CHIMERAS            = 0b0001
UCHIME_COMMAND = (constants.uchime_running_path + 
                             " --input %(input)s --uchimeout %(output)s")


not_rna = re.compile(r'[^ACGT]')

def keys_dict(keys):
    """Reads a keyfile and returns a dict with sample ids as keys and {"barcode":bar, "primer":primer} as values"""
    samples = {}
    
    for line in keys:
        if line.startswith("#"):
            continue
        sid, bar, primer = line.strip().split()[:3]
        if sid in samples:
            msg = "Sample name %s appears multiple times in keyfile. Aborting.\n" % sid
            sys.stderr.write(msg)
            raise ValueError(msg)
        else:
            samples[sid] =  {"barcode":bar, "primer":primer}

    for s in samples:
        samples[s]["primer"] = not_rna.sub('.', samples[s]["primer"])

    return samples

def stripped(fas, codes_primers,
             mode=STRIP_BARCODES_PRIMERS, max_excluded=0.9):
    """
    fas: an open fasta file
    codes_primers: an open keyfile
    mode: see Odd cases below
    max_excluded: If more than max_excluded would be excluded from output (Due to missing ID in keyfile or missing barcode/primer), they will be added to the end with a warning

    Odd cases:
    sequence id not in keyfile: throw out sequence, warn
    sequence does not start with barcode: ignore 
    sequence does not match primer:
        conservative mode - throw out 
        liberal mode - ignore (whole operation is idempotent in liberal mode)

    returns a generator over the stripped sequences
    """
    if not (STRIP_BARCODES_PRIMERS & mode):
        raise ValueError("framework.tools.fasta.stripped was called with an invalid mode (STRIP_BARCODES_PRIMERS & mode is false)")
    liberal = STRIP_BARCODES_PRIMERS & mode
    
    samples = keys_dict(codes_primers)
    total_seqs = 0
    excluded = deque()
    
    for s in seqs(fas):
        total_seqs += 1
        seq_id = s.split()[0].strip('>')

    #Find which sample this seq is from. We use the longest part of the sequence id
    #that contains the beginning of the id and matches a sample name.
        sample_name = ''
        id_len = len(seq_id)
        for i in xrange(id_len):
            if seq_id[0:id_len-i] in samples:
                sample_name = seq_id[0:id_len-i]
                break

        
        head = s.split("\n")[0]
        molecule = s[len(head)+1:]
        if sample_name == '':
            sys.stderr.write('WARNING: No sample name match for %s. Read ignored.\n' % seq_id)
            excluded.append(head.strip()+"\n"+molecule.strip()+"\n")
        else:#strip barcode/primer TODO should use startswith/replace instead of re
            barcode = re.compile("^"+samples[sample_name]["barcode"])
            primer = re.compile("^"+samples[sample_name]["primer"])
            molecule = barcode.sub('',molecule)
            primer_found = primer.match(molecule)
            molecule = primer.sub('',molecule)
            if primer_found or liberal:
                stripped_seq = head.strip()+"\n"+molecule.strip()+"\n"
                yield stripped_seq
            else:
                excluded.append(head.strip()+"\n"+molecule.strip()+"\n")
                

    percent = float(len(excluded))/total_seqs
    
    if percent > max_excluded:
        yield ";The following %d sequences should be excluded due to either missing ID in keyfile or missing barcode/primer.\n;They are included because this would exclude more than %s%% of sequences.\n" % (len(excluded),str(max_excluded))
        for s in excluded:
            yield s
    else:
        yield ";Sequences excluded due to either missing ID in keyfile or missing barcode/primer:\n;excluded: %d/%d\n" % (len(excluded), total_seqs)

def strip_homopolymers(seqs, n=6):
    homo = re.compile(r"(A{{{0},}}|G{{{0},}}|T{{{0},}}|C{{{0},}})".format(n))
    for s in seqs:
        yield homo.sub('',s)

def chimera_check(_seqs, threshold = 0.3):
    """ Returns the seqs, minus any sequences identified chimeric.
    This may take quite a while"""

    def get_label(s):
        return s.split()[0].strip(">")
    comments = {}
    
    tmp_file = os.path.join(constants.temp_files_dir, str(time.time()))
    uchime_out = os.path.join(constants.temp_files_dir, "uOut_"+str(time.time()))
    out = open(tmp_file,'w')
    for seq in _seqs:
        seq = seq.split("\n")
        for line in seq:
            if line.strip() != '':
                out.write(line.strip() +
                          (" /ab=01/\n" if line.startswith(">") else "\n"))
    out.close()

    cmd = UCHIME_COMMAND % {"input":tmp_file,"output":uchime_out}
    args = shlex.split(cmd)
    subprocess.call(args)

    chimeras = set()
    for line in open(uchime_out):
        line = line.split('\t')
        score, label = float(line[0]), line[1]#.strip()? split()[0]?
        if score > threshold:
            chimeras.add(label)
    chims = 0
    for seq in seqs(open(tmp_file), include_comments = True):
        if get_label(seq) not in chimeras or seq.startswith(';'):
            yield seq
        else:
            yield ";Sequence %s is suspected of being chimeric and was excluded" % get_label(seq)
            chims += 1
    yield ";%d chimeras found" % chims

def fasta_qa_preprocess(mode, fasta_path, codes_primers,
                        homopolymer_length=None):
    """Runs QA steps to remove primers, barcodes, homopolymers and chimeras from the data.
    ARGS:
        -mode: bitwise or of 0-n of the constants at the top of this file
        -fasta_path: the file to be preprocessed
        -codes_primers: the "keyfile". Also a list of lines will work, as it is
        used like: `for l in codes_primers`
        -homopolymer_length: the maximum lenght of a repeated nucleotide that can
        be kept
        -
        """
    mode = mode if mode else 0

    if mode  & STRIP_BARCODES_PRIMERS:
        result = stripped(open(fasta_path),
                              codes_primers,#keyfile. see above
                              mode)
        if mode & REMOVE_HOMOPOLYMERS:
            result = strip_homopolymers(result,
                                        n=homopolymer_length)
    elif mode & REMOVE_HOMOPOLYMERS:#homopolymers but not codes/primers
        raise ValueError(
            "Removing homopolymers requires removing barcodes and primers")
    else:
        result = open(fasta_path)

    if mode & REMOVE_CHIMERAS:
        result = chimera_check(result)
        
    return result

################################################################################
if __name__ == '__main__':
    if len(sys.argv) < 3:
        sys.stderr.write("Usage: %s keyfile.txt fastafile.fna [mode]\n" % sys.argv[0])
        sys.exit(-1)

    keys  = open(sys.argv[1])
    fasta = open(sys.argv[2])

    is_liberal = STRIP_LIBERAL if len(sys.argv) > 3 else 0
    mode = 0b1000 | is_liberal

    stripped_seqs = stripped(fasta,keys,mode=mode)

    for seq in stripped_seqs:
        sys.stdout.write(seq)
