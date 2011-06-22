#!/usr/bin/python
# -*- coding: utf-8 -*-

from django import forms

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
