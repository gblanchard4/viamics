

import sys
import os
import shlex
import subprocess

sys.path.append('../..')

cmd = "blastn -query %(fasta)s -outfmt %(fmt)d -num_alignments %(num)d -db %(blast_db)s -out %(blast_out)s"

def run_blastn(sequences_path,blast_output_path,blast_db_path,fmt=7,num=5,error_log='/tmp/error_log'):
    """Runs blastn on the fasta file at sequences_path against the db at blast_db_path. Blocks until blast is finished. The blastn executable is assumed to be on the path"""
    #cur_dir = os.getcwd()
    #os.chdir(rdp_running_path)

    command = (cmd % {'fasta':sequences_path, 'blast_out':blast_output_path, 'blast_db':blast_db_path,'fmt':fmt, 'num':num})
    print command
    args = shlex.split(command)
    ret_val = subprocess.call(args, stderr=open(error_log,'w'))
    #ret_val = os.system(cmd % {'fasta_file': fasta_file, 'rdp_output_file': rdp_output_file, 'error_log': error_log})
    #os.chdir(cur_dir)
    return (ret_val, error_log)



        
    
