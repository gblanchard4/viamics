import os
import sys
import base64
import socket
import cPickle
import zlib

from django.http import HttpResponse
from django.template.loader import get_template
from django.template import Context

sys.path.append("/clients")
sys.path.append("../")
from framework import constants

from framework import helper_functions
from framework.tools.logger import debug
from framework.clients.ferrisweb import webforms

server = helper_functions.server

def remove(id):
    server({ 'request': 'remove_analysis', 'analysis_id': id })
