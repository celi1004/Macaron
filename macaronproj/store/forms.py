from __future__ import unicode_literals
from django import forms
from .models import Macarons

class PhotoForm(forms.ModelForm):
    class Meta:
        model = Macarons
        fields = ('pic_title', 'picture', )
    
    # def __init__(self, *args, **kwargs):
    #     super(PhotoForm, self).__init__(*args, **kwargs)
    #     self.fields['picture'].required = False