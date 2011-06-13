import os

from framework.tools.helper_functions import SerializeToFile, DeserializeFromFile
from framework.tools.logger import debug
import framework.constants as c
import framework.tools.blast
import framework.tools.helper_functions as helper_functions

def _exec(p, request_dict):
    p.set_analysis_type('blast')
    
    separator = request_dict['seperator']#sic
    debug("storing separator: '%s'" % separator, p.files.log_file)
    open(p.files.seperator_file_path, 'w').write(separator)
    debug("storing DB name: '%s'" % request_dict['db_name'], p.files.log_file)
    open(p.files.blast_db_name_path, 'w').write(request_dict['db_name'])
    
    #run blast on data
    num_seqs = helper_functions.get_number_of_lines(p.files.data_file_path) / 2
    blast_db = os.path.join(c.blastdb_dir,request_dict['db_name'])
    
    debug(("running blast on %d sequences against database: %s " % (num_seqs, request_dict['db_name'])), p.files.log_file)
    framework.tools.blast.run_blastn(p.files.data_file_path, p.files.blast_output_file_path, blast_db,num=1)


    
    
    samples_dictionary(p)
    samples = DeserializeFromFile(p.files.samples_serialized_file_path).keys()
    open(p.files.all_unique_samples_file_path, 'w').write('\n'.join(samples) + '\n')
    debug("%d unique sample names stored" % len(samples), p.files.log_file)
    otu_library(p)


def samples_dictionary(p):
    debug("Computing sample dictionary", p.files.log_file)
    legend_path = os.path.join(c.blastdb_dir,
                               open(p.files.blast_db_name_path).read()+c.blast_legend_file_extension)
    samples_dict = framework.tools.blast.create_samples_dictionary(p.files.blast_output_file_path,
                                                                   legend_path,
                                                                   open(p.files.seperator_file_path).read())
    debug("Serializing samples dictionary object", p.files.log_file)
    SerializeToFile(samples_dict, p.files.samples_serialized_file_path)

def otu_library(p):
    debug("Generating OTU Library", p.files.log_file)
    legend_path = os.path.join(c.blastdb_dir,
                               open(p.files.blast_db_name_path).read()+c.blast_legend_file_extension)
    otu_library = framework.tools.blast.get_otu_library(p.files.blast_output_file_path,
                                                        legend_path,
                                                        open(p.files.seperator_file_path).read())
    SerializeToFile(otu_library, p.files.otu_library_file_path)



def _module_functions(p, request_dict):
    return {
        'qpcr_01': {'func': samples_dictionary, 'desc': 'Samples dictionary'},
        'qpcr_02': {'func': otu_library, 'desc': 'OTU library'}
    }

def _sample_map_functions(p, request_dict):
    return {}
