#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
import sys
import zlib
import base64
import socket
import cPickle

import unittest

sys.path.append("../../")

from framework import constants as c
from framework.tools import helper_functions


class Tests(unittest.TestCase):
    def setUp(self):
        self.socket_name = c.socket_name
        self.rdp_analysis_dir = os.path.join(c.analyses_dir, "b7782ab61207929a9e8a2f12eb52b977800d8979-test")
        self.test_fasta_file = os.path.join(c.base_dir, "../", 'unittests/test_files/example_fasta')
        self.analysis_id = helper_functions.get_sha1sum(self.test_fasta_file) + "-test"


    def server(self, request):
        return helper_functions.server(request)

    def testFrameworkStatus(self):
        server_request = {'request': 'status'}
        server_response = self.server(server_request)
        if server_response == {}:
            self.fail("Framework is not running..")

        self.assertTrue(server_response.has_key('response'))
        self.assertTrue(server_response.has_key('running_analyses'))
        self.assertTrue(server_response.has_key('done_analyses'))

    def testServerError(self):
        server_request = {'request': 'exec_analysis',
                          'analysis_type': u'bad_value',
                          'job_description': u'test',
                          'seperator': u'_',
                          'data_file_sha1sum': self.analysis_id,
                          'data_file_path': self.test_fasta_file,
                          'return_when_done': True}
        response = helper_functions.server(server_request)
        self.assertTrue(response['response'] == 'error')
        self.assertFalse(os.path.exists(self.rdp_analysis_dir))

    def testRepeatAnalysis(self):
        state = helper_functions.server({'request':'get_analyses'})
        n = len(state['analyses'])
        #test analysis not already present:
        self.assertFalse(os.path.exists(self.rdp_analysis_dir))
        
        server_request = {'request': 'exec_analysis',
                          'analysis_type': u'rdp',
                          'job_description': u'test',
                          'seperator': u'_',
                          'data_file_sha1sum': self.analysis_id,
                          'data_file_path': self.test_fasta_file,
                          'return_when_done': True}

        helper_functions.server(server_request)
        #request was executed:
        self.assertTrue(os.path.exists(self.rdp_analysis_dir))

        state = helper_functions.server({'request':'get_analyses'})
        self.assertTrue(len(state['analyses']) == n+1) 
        #try to run the analysis again:
        server_response = helper_functions.server(server_request)
        #len should still be n+1:
        self.assertTrue(len(state['analyses']) == n+1)
        #clean up:
        rm_request = {'request': 'remove_analysis',
                          'analysis_id': self.analysis_id}
        helper_functions.server(rm_request)
        state = helper_functions.server({'request':'get_analyses'})
        #remove was successful:
        self.assertTrue(len(state['analyses']) == n)
        print "state " + str(state)
        
        

        

