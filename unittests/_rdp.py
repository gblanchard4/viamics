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
        self.rdp_analysis_dir = os.path.join(c.analyses_dir, self.analysis_id)

        self.test_files = [self.test_fasta_file,
                           self.confidence,
                           self.QA_test_fasta]+self.split_analysis

    def tearDown(self):

        for t in self.test_files:
            self.server({'request': 'remove_analysis',
                     'analysis_id': helper_functions.get_sha1sum(t)+'-test'})


    def server(self, request):
        if os.environ.get("data_format") == "json":
            return helper_functions.server_json(request)
        else:
            return helper_functions.server(request)

    def analysis_complete(self,id):
        analysis_dir = os.path.join(c.analyses_dir, id)

        self.assertTrue(os.path.exists(analysis_dir))
        
        images = ['simpsons_diversity_index.png',
                  'rarefaction_all_samples.png',
                  'rdp_confidence_per_sample.png',
                  'rdp_confidence.png',
                  'samples_sequences_bar.png',
                  'shannon_diversity_index.png',]
        for i in images:
            self.assertTrue(os.path.exists(os.path.join(analysis_dir,i)),
                            msg="Failed to find:" + i)
            
        files = ['otu_library',
                 'rarefaction_dict',
                 'rdp_output',
                 'taxa_color_dict',
                 'samples_dict_serialized',
                 'type_of_analysis',
                 'unique_sample_names']
        for f in files:
            self.assertTrue(os.path.exists(os.path.join(analysis_dir,f)))

        dirs = ['maps',
                'piecharts',
                'rarefaction',
                'type_specific_figures']
        for d in dirs:
            self.assertTrue(os.path.exists(os.path.join(analysis_dir, d)))
        

    def testRDP(self):
        server_request = {'request': 'exec_analysis',
                          'analysis_type': u'rdp',
                          'job_description': u'test',
                          'seperator': u'_',
                          'data_file_sha1sum': self.analysis_id,
                          'data_file_path': self.test_fasta_file,
                          'return_when_done': True}
        server_response = self.server(server_request)
        self.assertTrue(os.path.exists(self.rdp_analysis_dir))

        self.analysis_complete(self.analysis_id)

        server_request = {'request': 'remove_analysis',
                          'analysis_id': self.analysis_id}
        server_response = self.server(server_request)

        self.assertFalse(os.path.exists(self.rdp_analysis_dir))

    def testAppend(self):
        initial = self.split_analysis[0]
        append = self.split_analysis[1]
        id = helper_functions.get_sha1sum(initial)+'-test'
        
            #create the analysis:
        self.server({'request':'exec_analysis','data_file_sha1sum':id,'data_file_path':initial,'seperator':':','job_description':'cat-test','analysis_type':'rdp','return_when_done': True})
        i = self.server({'request':'info','resource':'analysis','analysis_id':id})
        self.assertTrue(len(i['info']['all_unique_samples_list']) == 1)
        
            #append samples:
        self.server({'request':'append_samples_to_analysis','analysis_id':id,'data_file_path':append,'return_when_done':True})
        i = self.server({'request':'info','resource':'analysis','analysis_id':id})
        self.assertTrue(len(i['info']['all_unique_samples_list']) == 2)
        
            #clean up:
        self.server({'request': 'remove_analysis',
                     'analysis_id': id})

    def testLowConfidence(self):
        count_seqs = lambda f: sum(1 for l in f if l.startswith('>'))
        id = helper_functions.get_sha1sum(self.confidence)+'-test'

        #also you can check the samples_dict to count how many were classified
        self.server({'request':'exec_analysis','data_file_sha1sum':id,'data_file_path':self.confidence,'seperator':'_','job_description':'confidence test','analysis_type':'rdp','return_when_done': True,'threshold':0.8})
        i = self.server({'request':'info','resource':'analysis','analysis_id':id})
        n_low = count_seqs(open(os.path.join(c.analyses_dir,id,c.low_confidence_seqs_file_name)))
        path = self.server({'request':'get_samples_dict_path','analysis_id':id})['samples_dict_path']
        samples_dict = cPickle.load(open(path))
        total_classified = 0
        for _sample in samples_dict.values():
            sample = _sample['genus']
            total_classified += sum([sample[genus] for genus in sample if ':' not in genus]) 
        self.assertTrue(n_low == 10)
        self.assertTrue(n_low + total_classified == 20)
        self.server({'request': 'remove_analysis',
                     'analysis_id': id})

        
        self.server({'request':'exec_analysis','data_file_sha1sum':id,'data_file_path':self.confidence,'seperator':'_','job_description':'confidence test','analysis_type':'rdp','return_when_done': True,'threshold':0.9999})
        i = self.server({'request':'info','resource':'analysis','analysis_id':id})
        n_low = count_seqs(open(os.path.join(c.analyses_dir,id,c.low_confidence_seqs_file_name)))
        print 'should be 11: '+str(n_low)
        self.assertTrue(n_low == 11)#expect occasional random failure
        self.server({'request': 'remove_analysis',
                     'analysis_id': id})

    def testStrip(self):
        id = helper_functions.get_sha1sum(self.QA_test_fasta)+'-test'
        keyfile = open(self.QA_keyfile).readlines()
        
        
        self.server({'request':'exec_analysis',
                     'data_file_sha1sum':id,
                     'data_file_path':self.QA_test_fasta,
                     'seperator':'_',
                     'job_description':'QA test',
                     'analysis_type':'rdp',
                     'codes_primers':keyfile,
                     "qa_mode":fasta.STRIP_BARCODES_PRIMERS,
                     'return_when_done': True,
                     })
        i = self.server({'request':'info',
                         'resource':'analysis',
                         'analysis_id':id})
        while(True):
            dat = open(os.path.join(c.analyses_dir,id,'log'))
            try:                
                dat.read().index("Filling job description")
                dat.close()
                break
            except:
                dat.close()

        correct = helper_functions.get_sha1sum(self.QA_result)
        framework = helper_functions.get_sha1sum(self.QA_test_fasta)
        
        #self.analysis_complete(id)
                    
