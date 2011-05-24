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
# Web client core. Talks to the server, generates web pages for analyses.
#


import os
import sys
import json
import base64
import socket
import cPickle
import zlib

from django.http import HttpResponse
from django.template.loader import get_template
from django.template import Context

sys.path.append("../..")
sys.path.append("../../..")
from framework import constants

from framework.tools import helper_functions
from framework.tools.logger import debug
from framework.clients.ferrisweb import webforms

server = helper_functions.server

def server_err(server_dict):
    if server_dict.has_key('response'):
        return server_dict['response'] == 'error'
    else:
        return True

def err_response(server_dict):
    context_dict = {}

    if server_dict.has_key('content'):
        context_dict['content'] =  server_dict['content']
    if server_dict.has_key('exception'):
        context_dict['exception'] =  server_dict['exception']
    if server_dict.has_key('time_stamp'):
        context_dict['time_stamp'] = server_dict['time_stamp']
    if not len(server_dict):
        context_dict['content'] =  "Either server is not running or socket name is wrong"

    return HttpResponse(get_template("error.tmpl").render(Context(context_dict)))


#please read before modifying web api:
#http://en.wikipedia.org/wiki/Representational_State_Transfer#RESTful_web_services
def analyses(request):
    if request.method == 'GET':
        server_request = {'request': 'get_analyses'}
        server_response = server(server_request)
        
        if server_err(server_response):
            return err_response(server_response)
        
        analyses = server_response['analyses']
        return HttpResponse(json.dumps(analyses))
    else:
        return err_response({'content':'Only the GET method is implemented for this resource'})

"""    
def echo_file(request):
    if request.method == 'POST':
        f = request.FILES[request.FILES.keys()[0]]
        result = {}
        for line in f:
            l = line.split(',')
            result[l[0].strip()] = {"group":l[1].strip()}
        
        return HttpResponse(json.dumps(result))
"""
