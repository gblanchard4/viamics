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
        self.test_fasta_file = os.path.join(c.base_dir, "../", 'unittests/test_files/example_fasta')
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
        
