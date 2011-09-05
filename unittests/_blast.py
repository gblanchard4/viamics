#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
import sys
import zlib
import base64
import socket
import shutil
import cPickle

import unittest

sys.path.append("../../")

from framework import constants as c
from framework.tools import helper_functions, fasta


class Tests(unittest.TestCase):
    def setUp(self):
        J = lambda s: os.path.join(c.base_dir,'../','unittests/test_files',s)
        self.test_fasta_file = J('example_fasta')
        self.split_analysis = [J(s) for s in ['split1.fna','split2.fna']]
        self.confidence = J('confidence_levels.fas')
        self.QA_test_fasta = J("QA_test_fasta")
        self.QA_keyfile = J('QA_keyfile')
        self.QA_result = J('QA_stripped')
        self.analysis_id = helper_functions.get_sha1sum(self.test_fasta_file) + "-test"
        self.QA_id = helper_functions.get_sha1sum(self.QA_test_fasta) + "-test"
        self.rdp_analysis_dir = os.path.join(c.analyses_dir, self.analysis_id)
        self.QA_analysis_dir = os.path.join(c.analyses_dir, self.QA_id)

        self.test_files = [self.test_fasta_file,
                           self.confidence,
                           self.QA_test_fasta]+self.split_analysis

        #create db:
        self.db_name = "gg_coreset_test"
        blastdb_path = os.path.join(c.base_dir,'../',
                                    'unittests/test_files',
                                    self.db_name)
        
        self.server({'request':'new_blast_db',
                'data_file_path':blastdb_path,
                'db_name':self.db_name})

        #check db exists
        self.assertTrue(os.path.exists(os.path.join(c.blastdb_dir, self.db_name)))    
        
    def tearDown(self):
        
        for t in self.test_files:
            self.server({'request': 'remove_analysis',
                     'analysis_id': helper_functions.get_sha1sum(t)+'-test'})

        #remove db
        self.db_name = "gg_coreset_test"
        
        self.server({"request":"delete",
                "resource":"blastdb",
                "id":self.db_name})
        #check db was deleted
        self.assertFalse(os.path.exists(os.path.join(c.blastdb_dir, self.db_name))) 

            

    def server(self, request):
        return helper_functions.server(request)

    def analysis_complete(self,id):
        analysis_dir = os.path.join(c.analyses_dir, id)

        self.assertTrue(os.path.exists(analysis_dir))
        
        images = ['simpsons_diversity_index.png',
                  'shannon_diversity_index.png',]
        for i in images:
            self.assertTrue(os.path.exists(os.path.join(analysis_dir,i)),
                            msg="Failed to find:" + i)
            
        files = ['otu_library',
                 'blast_output',
                 'taxa_color_dict',
                 'samples_dict_serialized',
                 'type_of_analysis',
                 'unique_sample_names']
        for f in files:
            self.assertTrue(os.path.exists(os.path.join(analysis_dir,f)))

        dirs = ['maps',
                'piecharts',
                'type_specific_figures']
        for d in dirs:
            self.assertTrue(os.path.exists(os.path.join(analysis_dir, d)))



    def testBLAST(self):
        
        #run analysis:        
        server_request = {'request': 'exec_analysis',
                          'analysis_type': u'blast',
                          'job_description': u'testBLAST',
                          'seperator': u'_',
                          'db_name':self.db_name,
                          'data_file_sha1sum': self.QA_id,
                          'data_file_path': self.QA_test_fasta,
                          'return_when_done': True}
        server_response = self.server(server_request)
        self.assertTrue(os.path.exists(self.QA_analysis_dir))

        self.analysis_complete(self.QA_id)

        #remove analysis:
        server_request = {'request': 'remove_analysis',
                          'analysis_id': self.QA_id}
        server_response = self.server(server_request)

        #check analysis was deleted
        self.assertFalse(os.path.exists(self.QA_analysis_dir))


    def testStripBLAST(self):
        id = helper_functions.get_sha1sum(self.QA_test_fasta)+'-test'
        keyfile = open(self.QA_keyfile).readlines()
        
        self.server({'request':'exec_analysis',
                     'data_file_sha1sum':id,
                     'data_file_path':self.QA_test_fasta,
                     'job_description': u'testBLAST',
                     'seperator': u'_',
                     'db_name':self.db_name,
                     'analysis_type':'blast',
                     'codes_primers':keyfile,
                     "qa_mode":fasta.STRIP_BARCODES_PRIMERS,
                     #'return_when_done': True,
                     })
        i = self.server({'request':'info',
                         'resource':'analysis',
                         'analysis_id':id})
        while(True):#read log file to see if analysis is past QA stage
            dat = open(os.path.join(c.analyses_dir,id,'log'))
            try:                
                dat.read().index("Filling job description")
                dat.close()
                break
            except:
                dat.close()

        correct = helper_functions.get_sha1sum(self.QA_result)
        framework = helper_functions.get_sha1sum(self.QA_test_fasta)
