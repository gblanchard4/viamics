#!/usr/bin/python
# -*- coding: utf-8 -*-

import unittest
import sys
import os

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
    args = iter(sys.argv)
    json_format = False
    while(True):
        try:
            a = args.next()
            if a == "-d":
                form = args.next()
                json_format = form if form == "json" else None
                break
        except StopIteration:
            break
        
    if json_format:
        print "using json data format"
        os.environ["data_format"] = "json"
    
    unittest.TextTestRunner(verbosity=3).run(__suite())
