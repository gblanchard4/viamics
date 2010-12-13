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
import merensframework.constants as c

class Tests(unittest.TestCase):
    def setUp(self):
        #append directories to the list as constants file grow
        self.dirs_in_constants = ['base_dir', 'error_logs_dir', 'analyses_dir',
                                  'rdp_running_path', 'temp_files_dir', 'web_dir',
                                  'web_statics_dir', 'templates_dir']

        self.vars_in_constants = ['socket_name']

    def testDirectories(self):
        def _test(dir):
            if not c.__dict__.has_key(dir):
                raise("'%s' has no entry in constants" % dir)

            if not os.path.exists(c.__dict__[dir]):
                raise("'%s' doesn't exist at '%s'" % (dir, c.__dict__[dir]))

            return True

        for dir in self.dirs_in_constants:
            self.assertTrue(_test(dir))

    def testVariables(self):
        def _test(var):
            if not c.__dict__.has_key(var):
                raise("'%s' has no entry in constants" % dir)

            if not len(c.__dict__[var]) > 0:
                raise("'%s' variable is null" % var)

            return True

        for var in self.vars_in_constants:
            self.assertTrue(_test(var))



