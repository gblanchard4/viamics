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
from framework.clients.ferrisweb.views import server_err, err_response

server = helper_functions.server

def server_resp_json(server_request):
    server_response = server(server_request)
    return HttpResponse(json.dumps(server_response))


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

def get_low_confidence_seqs():

    file_path = os.path.join(constants.analyses_dir, analysis_id,constants.low_confidence_seqs_file_name)
    
    if (os.path.exists(file_path)):
        response = HttpResponse(FileWrapper(open(file_path)))
        response['Content-Disposition'] = 'attachment; filename=low-confidence.fas'
    else:
        response = HttpResponse("file not found", status=404)

    return response



def blastdbs(request):
    #import pdb; pdb.set_trace()
    
    if request.method == 'GET':
        req = {'request':'list', 'resource':'blastdb'}
        res = server(req)
        return(HttpResponse(json.dumps(res['resources'])))
        #return server_resp_json(req)
    
    elif request._method == 'POST':
        return blast_request(request,'new_blast_db')
        


def blastdb(request, db_name):
    #import pdb; pdb.set_trace()
    if request.method == 'GET':
        #server({'request':'info','resource':'blastdb','id':<id>})
        return HttpResponse(json.dumps({'GET request':'recieved'}))
    elif request._method == 'DELETE':
        req = {'request':'delete', 'id':db_name, 'resource':'blastdb'}
        return server_resp_json(req)
    elif request._method == 'POST':
        return blast_request(request, 'append_seqs_to_blastdb')
        
            
def blast_request(request, req_type):
    if len(request.FILES)>0:#uploaded file
        #import pdb;pdb.set_trace()
        tmp_data_file = os.path.join(constants.temp_files_dir,request.POST['db_name'].replace(' ',"_"))
        f = open(tmp_data_file,'w')
        f.write(request.FILES[request.FILES.keys()[0]].read())
        f.close()
        if request.POST['file_type'] == 'fasta':
            req = {'request':req_type,'data_file_path':tmp_data_file,'db_name':request.POST['db_name']}
            r = server_resp_json(req)
            os.unlink(tmp_data_file)
            return r
        
        elif request.POST['file_type'] == 'blast_db':
            pass#TODO basically just give the file to the server and let it save it.
    else:
        return HttpResponse(json.dumps({'response':'error','content':'please select a file to upload'}))
