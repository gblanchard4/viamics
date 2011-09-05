#!/usr/bin/python
# -*- coding: utf-8 -*-

import unittest

#unittest declerations
import _sanity
import _framework
import _rdp
import _blast

def __suite():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(_sanity.Tests))
    suite.addTest(unittest.makeSuite(_rdp.Tests))
    suite.addTest(unittest.makeSuite(_framework.Tests))
    suite.addTest(unittest.makeSuite(_blast.Tests))

    return suite

if __name__ == "__main__":
    unittest.TextTestRunner(verbosity=3).run(__suite())
