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
# Django urls for web client of the framework.
#


import sys
sys.path.append("../..")
sys.path.append("../../..")

from framework import constants

from django.conf.urls.defaults import *

from clients.ferrisweb.views import index
from clients.ferrisweb import web_api
from clients.ferrisweb.views import about
from clients.ferrisweb.views import status_request
from clients.ferrisweb.views import analysis_info
from clients.ferrisweb.views import analysis_dendrograms
from clients.ferrisweb.views import confidence_per_otu
from clients.ferrisweb.views import refresh_analysis_files
from clients.ferrisweb.views import create_sample_map
from clients.ferrisweb.views import heatmap_detail
from clients.ferrisweb.views import dendrogram_detail
from clients.ferrisweb.views import refresh_sample_map
from clients.ferrisweb.views import sample_map_instance
from clients.ferrisweb.views import sample_map_instances
from clients.ferrisweb.views import sample_map_dot
from clients.ferrisweb.views import new_analysis
from clients.ferrisweb.views import update_analysis_append_samples
from clients.ferrisweb.views import update_analysis_remove_samples
from clients.ferrisweb.views import split_fasta
from stripper.views import strip_split

urlpatterns = patterns('',
    (r'^$', index),
    (r'^api/analyses', web_api.analyses),#this should be specified in greater detail if we want
    #to decouple clients. right now it just gives the json for get_analyses.
    #maybe a betterway would be to allow say, GET viamics.com/index.json
    (r'^about/$', about),
    (r'^status/$', status_request),
    (r'^info/(?P<analysis_id>[a-zA-Z0-9_.-]+)/$', analysis_info),
    (r'^info/(?P<analysis_id>[a-zA-Z0-9_.-]+)/dendrograms/$', analysis_dendrograms),
    (r'^info/(?P<analysis_id>[a-zA-Z0-9_.-]+)/confidence/genus/$', confidence_per_otu),
    (r'^info/(?P<analysis_id>[a-zA-Z0-9_.-]+)/(?P<instance>\d+)/heatmap/(?P<rank>[a-zA-Z]+)/$', heatmap_detail),
    (r'^info/(?P<analysis_id>[a-zA-Z0-9_.-]+)/(?P<instance>\d+)/dendrogram/(?P<rank>[a-zA-Z]+)/$', dendrogram_detail),
    (r'^maps/(?P<analysis_id>[a-zA-Z0-9_.-]+)/$', sample_map_instances),
    (r'^maps/(?P<analysis_id>[a-zA-Z0-9_.-]+)/(?P<instance>\d+)/$', sample_map_instance),
    (r'^maps/(?P<analysis_id>[a-zA-Z0-9_.-]+)/(?P<instance>\d+)/dot/(?P<rank>[a-zA-Z]+)/$', sample_map_dot),
    (r'^maps/(?P<analysis_id>[a-zA-Z0-9_.-]+)/(?P<instance>\d+)/dot/(?P<rank>[a-zA-Z]+)/(?P<real_abundance>[a-zA-Z]+)/$', sample_map_dot),
    (r'^refresh/maps/(?P<analysis_id>[a-zA-Z0-9_.-]+)/(?P<instance>\d+)/$', refresh_sample_map),
    (r'^refresh/(?P<analysis_id>[a-zA-Z0-9_.-]+)/$', refresh_analysis_files),
    (r'^create_sample_map/(?P<analysis_id>[a-zA-Z0-9_.-]+)/(?P<step>\d+)$', create_sample_map),
    (r'^new/(?P<analysis_type>[a-zA-Z0-9_.-]+)/$', new_analysis),
    (r'^update_samples/(?P<analysis_id>[a-zA-Z0-9_.-]+)/append/$', update_analysis_append_samples),
    (r'^update_samples/(?P<analysis_id>[a-zA-Z0-9_.-]+)/remove/$', update_analysis_remove_samples),
    (r'^media/(?P<analysis_id>[a-zA-Z0-9_.-]+)/split_fasta/$',split_fasta),
    (r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': constants.analyses_dir, 'show_indexes': True}),
    (r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': constants.web_statics_dir, 'show_indexes': True}),
    (r'^stripsplit/$', strip_split)

)
