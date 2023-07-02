from django import forms
from multiupload.fields import MultiFileField

class MultiImageUploadForm(forms.Form):
    images = MultiFileField(max_num=10, min_num=1, max_file_size=1024*1024*5)

