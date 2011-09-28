#!/usr/bin/python
# -*- coding: utf-8 -*-

from decimal import Decimal as D
from django import forms
from framework.tools import helper_functions
from framework.tools import fasta


class AllFastaUploadForm(forms.Form):
    error_css_class = "error_field"
    job_description = forms.CharField(max_length = 256)
    seperator = forms.CharField(max_length = 1)
    strip = forms.BooleanField(label="Strip barcodes and primers?",
                               initial=True,
                               required=False)
    keyfile = forms.Field(label="Keyfile (barcodes and primers)",
                          widget=forms.FileInput(),
                          required=False)
    strip_mode = forms.ChoiceField(choices=[(0,
                                             "conservative"),
                                             (fasta.STRIP_LIBERAL,"liberal")],
                                   label="mode",
                                   help_text="Conservative mode discards sequences"
                                             " if the barcode and primer are not "
                                   "found. Liberal mode keeps them unchanged.",
                                   required=False)
    
    homopolymers = forms.BooleanField(label="Strip homopolymers?",
                                      initial=True,
                                      required=False)
    homopolymer_length = forms.IntegerField(label="Max homopolymer length",
                                      initial=6,
                                      widget = forms.TextInput(attrs={"size":10}),
                                      required=False)
    chim = forms.BooleanField(label="Remove chimeras?",
                              initial=False,
                              required=False)
    data_file = forms.Field(widget=forms.FileInput(),
                            required=True)
    
    
    def clean(self):
        #import pdb;pdb.set_trace()
        cleaned_data = self.cleaned_data
        keyfile = cleaned_data["keyfile"]
        if cleaned_data.get('strip') and not keyfile:
            e = self.error_class(["Stripping primers and barcodes requires "
                                        "a keyfile. Often this file will have a "
                                        "name ending in '_mapping.txt'"])
            self._errors["keyfile"]  = e
        strip = fasta.STRIP_BARCODES_PRIMERS if cleaned_data.get("strip") else 0
        
        if cleaned_data.get('strip_mode'):
            strip_mode = int(cleaned_data["strip_mode"])
        else:
            strip_mode = 0
        
        if cleaned_data.get("homopolymers"):
            homopolymers = fasta.REMOVE_HOMOPOLYMERS
            if not cleaned_data.get('homopolymer_length'):
                e = self.error_class(["Please provide a minimum homopolymer"
                                            " length. Any repeated sequence of "
                                            "nucleotides longer than the minimum"
                                            " will be removed"])
                self._errors["homopolymer_length"] = e
        else:
            homopolymers = 0
            
        if cleaned_data.get('chim'):
            chimeras = fasta.REMOVE_CHIMERAS
        else:
            chimeras = 0

        cleaned_data["qa_mode"] = strip | strip_mode | homopolymers | chimeras
        if keyfile:
            cleaned_data["codes_primers"] = keyfile.readlines()

        return cleaned_data


class BlastUploadForm(AllFastaUploadForm):
    CREATE_URL = "/new/blast/"
    

    def __init__(self, *args, **kwargs):
        super(BlastUploadForm, self).__init__(*args, **kwargs)
        req = {'request':'list','resource':'blastdb'}
        resp = helper_functions.server(req)
        self.fields['db_name'] = forms.ChoiceField(choices=[(r['id'],r['id']) for r in resp['resources']])
        
class FastaUploadForm(AllFastaUploadForm):
    CREATE_URL = "/new/rdp/"
    
    threshold = forms.DecimalField(max_value = D(1),
                                   min_value = D(0),
                                label = "Confidence threshold",
                                initial = D(0))

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
