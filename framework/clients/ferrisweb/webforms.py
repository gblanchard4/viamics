#!/usr/bin/python
# -*- coding: utf-8 -*-

from django import forms
from framework.tools import helper_functions


class BlastUploadForm(forms.Form):
    job_description = forms.CharField(max_length = 256)
    data_file = forms.Field(widget=forms.FileInput())
    seperator = forms.CharField(max_length = 1)
    #db_select = forms.ChoiceField( choices = [])

    def __init__(self, *args, **kwargs):
        super(BlastUploadForm, self).__init__(*args, **kwargs)
        req = {'request':'list','resource':'blastdb'}
        resp = helper_functions.server(req)
        self.fields['db_name'] = forms.ChoiceField(choices=[(r['id'],r['id']) for r in resp['resources']])
        

class FastaUploadForm(forms.Form):
    job_description = forms.CharField(max_length = 256)
    seperator = forms.CharField(max_length = 1)
    data_file = forms.Field(widget=forms.FileInput())

class QpcrUploadForm(forms.Form):
    job_description = forms.CharField(max_length = 256)
    data_file = forms.Field(widget=forms.FileInput())

class EnvUploadForm(forms.Form):
    job_description = forms.CharField(max_length = 256)
    data_file = forms.Field(widget=forms.FileInput())

class VampsUploadForm(forms.Form):
    job_description = forms.CharField(max_length = 256)
    data_file = forms.Field(widget=forms.FileInput())

class DataUploadForm(forms.Form):
    data_file = forms.Field(widget=forms.FileInput())

sample_field_attrs_dict = {'size': 10}

type_forms = {'blast' : BlastUploadForm,
              'qpcr'  : QpcrUploadForm,
              'rdp'   : FastaUploadForm,
              'env'   : EnvUploadForm}
