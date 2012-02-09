#!/usr/bin/env python

import sys, os, subprocess
from datetime import datetime

from pygments import highlight
from pygments.lexers import PythonLexer
from pygments.formatters import TerminalFormatter

ENDC = '\033[0m'
OKGREEN = '\033[31;40m'
NON_CODE = "\033[3;37m"



for f in os.listdir(sys.argv[1]):
    if not os.path.isdir(os.path.join(sys.argv[1],f)):
        print "_"*80
        
        print OKGREEN+datetime.fromtimestamp(float(f)).strftime("%A, %b %d %Y, %X %p")+":"+ENDC
        print "_"*80

        for line in open(os.path.join(sys.argv[1],f)).readlines():
            if line.strip().startswith("File"):
                sys.stdout.write( NON_CODE+line+ENDC)
            else:
                sys.stdout.write(highlight(line,PythonLexer(),
                                TerminalFormatter(bg="dark")))
        
