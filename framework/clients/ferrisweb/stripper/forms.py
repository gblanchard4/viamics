from django import forms


class RunStripperForm(forms.Form):
    fasta = forms.FileField()
    keys  = forms.FileField()
