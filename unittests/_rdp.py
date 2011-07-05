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
from framework.tools import helper_functions


class Tests(unittest.TestCase):
    def setUp(self):
        J = lambda s: os.path.join(c.base_dir,'../','unittests/test_files',s)
        self.test_fasta_file = J('example_fasta')
        self.split_analysis = [J(s) for s in ['split1.fna','split2.fna']]
        self.analysis_id = helper_functions.get_sha1sum(self.test_fasta_file) + "-test"
        self.rdp_analysis_dir = os.path.join(c.analyses_dir, self.analysis_id)

    def server(self, request):
        return helper_functions.server(request)

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

        images = ['rarefaction_all_samples.png', 'rdp_confidence_per_sample.png', 'rdp_confidence.png', 'samples_sequences_bar.png', 'shannon_diversity_index.png', 'simpsons_diversity_index.png']
        for i in images:
            try:
                img_path = os.path.join(self.rdp_analysis_dir, i)
                self.assertTrue(os.path.exists(img_path))
            except AssertionError as e:
                print img_path
                raise e
                

        files = ['otu_library', 'rarefaction_dict', 'rdp_output', 'taxa_color_dict', 'samples_dict_serialized', 'type_of_analysis', 'unique_sample_names']
        for f in files:
            self.assertTrue(os.path.exists(os.path.join(self.rdp_analysis_dir, f)))

        dirs = ['maps', 'piecharts', 'rarefaction', 'type_specific_figures']
        for d in dirs:
            self.assertTrue(os.path.exists(os.path.join(self.rdp_analysis_dir, d)))


        server_request = {'request': 'remove_analysis',
                          'analysis_id': self.analysis_id}
        server_response = self.server(server_request)
        for d in dirs:
            self.assertFalse(os.path.exists(os.path.join(self.rdp_analysis_dir, d)))
        self.assertFalse(os.path.exists(self.rdp_analysis_dir))

        def testAppend(self):
            initial = self.split_analysis[0]
            append = self.split_analysis[1]
            id = helper_functions.get_sha1sum(initial)+'-test'

            #create the analysis:
            server({'request':'exec_analysis','data_file_sha1sum':id,'data_file_path':initial,'seperator':':','job_description':'cat-test','analysis_type':'rdp','return_when_done': True})
            i = server({'request':'info','resource':'analysis','analysis_id':id})
            self.assertTrue(len(i['info']['all_unique_samples_list']) == 1)

            #append samples:
            server({'request':'append_samples_to_analysis','analysis_id':id,'data_file_path':append,'return_when_done':True})
            i = server({'request':'info','resource':'analysis','analysis_id':id})
            self.assertTrue(len(i['info']['all_unique_samples_list']) == 2)

            #clean up:
            server({'request': 'remove_analysis',
                    'analysis_id': id})

        
