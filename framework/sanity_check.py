#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (C) 2010 - 2011, University of New Orleans
#
# This program is free software; you can redistribute it and/or modify it under
# the terms of the GNU General Public License as published by the Free
# Software Foundation; either version 2 of the License, or (at your option)
# any later version.
#
# Please read the COPYING file.
#
# --
#
# Basic sanity check to make sure that everything is in place.
#


import os
import sys
import stat

sys.path.append("../")
from framework import constants as c
from framework.tools.helper_functions import confirm

def dirs():
    # base directory check:
    if not os.path.exists(c.base_dir):
        print "Error: Base directory does not exist ('%s'). Please make it sure that you have edited config.py correctly." % c.base_dir
        sys.exit(-1)
    elif not os.path.exists(os.path.join(c.base_dir, "server.py")):
        print "Error: Base directory has to point to the framework root. Please make it sure that you have edited config.py correctly."
        sys.exit(-1)

    # permissions check
    critical_777_dirs = {
            "Analyses dirirectory": c.analyses_dir,
            "Error logs directory": c.error_logs_dir,
            "Temporary files directory": c.temp_files_dir
            }

    missing_dirs = [dir for dir in critical_777_dirs if not os.path.exists(critical_777_dirs[dir])]

    if len(missing_dirs):
        print "Some directories are missing:\n"
        for dir in missing_dirs:
            print " * %s (%s)" % (dir, critical_777_dirs[dir])
        print

        if confirm("Would you like framework to create them?", resp=True):
            for dir in missing_dirs:
                os.makedirs(critical_777_dirs[dir])
            print "Done.\n"
        else:
            print "Exiting.\n"
            sys.exit(-1)

    wrong_perms = [dir for dir in critical_777_dirs if not os.stat(critical_777_dirs[dir])[stat.ST_MODE] & stat.S_IWOTH]

    if len(wrong_perms):
        print "Some directories have wrong permissions. Please make it sure that their permission set to 777:\n"
        for dir in wrong_perms:
            print " * %s (%s)" % (dir, critical_777_dirs[dir])
        print

        if confirm("Would you like framework to setup permissions?", resp=True):
            for dir in wrong_perms:
                os.chmod(critical_777_dirs[dir], 0777)
            print "Done.\n"
        else:
            print "Exiting.\n"
            sys.exit(-1)

def all():
    print "Checking dirs.."
    dirs()
    print "All O.K.\n\n"

if __name__ == "__main__":
    all()
