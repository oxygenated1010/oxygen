from django import forms
from .models import Postdata, Category




class PostForm(forms.ModelForm):
    class Meta:
        model = Postdata
        fields = ('title', 'title_tag', 'header_image', 'author', 'category', 'body') # header_image was added

        widgets= {
            'title':forms.TextInput(attrs={'class': 'form-control'}),
            'title_tag':forms.TextInput(attrs={'class': 'form-control'}),
            'author':forms.TextInput(attrs={'class': 'form-control','value': '','id': 'jay', 'type': 'hidden'}),
            'category':forms.TextInput(attrs={'class': 'form-control'}),
            #'author':forms.Select(attrs={'class': 'form-control'}),
            'body':forms.Textarea(attrs={'class': 'form-control'}),
            
        } 