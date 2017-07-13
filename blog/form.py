from django import forms
from django.forms import models

from .models import Post
from .models import UploadFileModel

class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title', 'text',)


class UploadFileForm(forms.ModelForm):
    class Meta:
        model = UploadFileModel
        fields = ('title', 'file', 'author')

    # def __init__(self, *args, **kwargs):
    #     # super(PostForm, self).__init__(*args, **kwargs)
    #     self.fields['file'].required = False