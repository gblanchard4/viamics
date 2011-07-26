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
    """Runs blastn on the fasta file at sequences_path against the db at blast_db_path. Blocks until blast is finished. The blastn executable is assumed to be on the path"""

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
    #error_log = os.path.join(c.blastdb_dir,name,c.blast_error_name)
    if error_log:
        error_log = open(error_log,'w')
    out = os.path.join(output_dir,name)
    command = makeblastdb_cmd % {"in":fasta_path, "out":out, "name":name,'input_type':input_type}
    print "\n\nrunning "+command
    args = shlex.split(str(command))
    exit_val = subprocess.call(args)
    return exit_val

class Blast_Result:

    def __init__(self, output, fmt=7):
        if fmt != 7 and fmt != 6:
            raise ValueError('Blast format %d is not supported yet' % fmt)
        output = [line.split('\t') for line in
                  filter(lambda l: not l.startswith('#'),output.strip().split('\n'))]
        for l in output:
            assert l[0] == output[0][0]
        self.id = output[0][0]
        self.alignments = [Alignment(l,fmt=fmt) for l in output]

class Alignment:

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
