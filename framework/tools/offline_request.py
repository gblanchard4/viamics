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
# A tool to run batch requests on the framework.
#

import os
import sys
import base64
import socket
import cPickle
import zlib

sys.path.append("../")
from framework import constants

from framework.tools import helper_functions

def server(request):
    serversocket = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
    try:
        serversocket.connect(constants.socket_name)
    except:
        return None

    serversocket.send(base64.encodestring(zlib.compress(cPickle.dumps(request), 9)))

    data = ""
    while True:
        chunk = serversocket.recv(512)
        data += chunk
        if chunk[-1] == "\n":
            break

    response = cPickle.loads(zlib.decompress(base64.decodestring(data)))
    serversocket.close()
    return response

def refresh_all_diversity_images():
    server_request = {'request': 'status', 'time_stamp': helper_functions.get_time_stamp()}
    server_response = server(server_request)
    for analysis_id in server_response['done_analyses']:
        print "Refreshing: ", analysis_id, "..."
        server_request = {'request': 'refresh_analysis_files', 'analysis_id': analysis_id, 'refresh_requests': ['diversity_bar_image', 'shannon_diversity_bar_image'], 'time_stamp': helper_functions.get_time_stamp(), 'return_when_done': True}
        server_response = server(server_request)
        print server_response['response']
        print



def refresh_all_sample_maps():
    server_request = {'request': 'status', 'time_stamp': helper_functions.get_time_stamp()}
    server_response = server(server_request)
    for analysis_id in server_response['done_analyses']:
        server_request = {'request': 'get_sample_map_instances', 'analysis_id': analysis_id, 'time_stamp': helper_functions.get_time_stamp()}
        server_response = server(server_request)
        for instance in server_response['instances']:
            print "Refreshing: ", analysis_id, instance, "..."
            server_request = {'request': 'refresh_sample_map', 'analysis_id': analysis_id, 'instance': instance, 'return_when_done': True, 'time_stamp': helper_functions.get_time_stamp()}
            server_response = server(server_request)
            print server_response['response']
            print

if __name__ == "__main__":
    refresh_all_diversity_images()
