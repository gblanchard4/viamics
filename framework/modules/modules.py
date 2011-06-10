#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys

sys.path.append("../")

import framework.constants as c

import framework.modules.rdp as rdp
import framework.modules.env as env
import framework.modules.qpcr as qpcr
import framework.modules.commons as commons
import framework.modules.blast as blast

server_modules_dict = {'rdp'    : rdp,
                       'qpcr'   : qpcr,
                       'env'    : env,
                       'commons': commons,
                       'blast'  : blastx}
