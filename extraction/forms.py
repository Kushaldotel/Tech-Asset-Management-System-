from django import forms

class UploadZipForm(forms.Form):
    zip_file = forms.FileField(label='Select a zip file')
