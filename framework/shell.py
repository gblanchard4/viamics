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
from framework import constants as c

from framework import helper_functions
from framework.tools.logger import debug
from framework.clients.ferrisweb import webforms
from framework.helper_functions import HeatmapOptions, SerializeToFile, DeserializeFromFile, GetCopy, RelativePath

server = helper_functions.server

# The following methods can be used for testing the server out

def get_analyses():
    l = server({'request':'get_analyses'})
    for x in l:
        print x, l[x]
    return

# supply the id you want to remove. I've supplied two shortcuts to two common ids from the sample data.

def remove(id):
    d = {'b':'b7782ab61207929a9e8a2f12eb52b977800d8979','a':'aa401d5f62a5d595ccdea3452dbba354e4fb195d'}
    if id in d:
        id=d[id]
    l = server({'request':'remove_analysis','analysis_id':id})
    for x in l:
        print x, l[x]
    return

def status():
    l = server({'request':'status'})
    for x in l:
        print x, l[x]
    return
