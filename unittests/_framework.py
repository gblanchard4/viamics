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
from framework import helper_functions


class Tests(unittest.TestCase):
    def setUp(self):
        self.socket_name = c.socket_name
        self.rdp_analysis_dir = os.path.join(c.analyses_dir, "b7782ab61207929a9e8a2f12eb52b977800d8979-test")

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

