from django.forms import ModelForm
from django import forms
from .models import Visitor

class VisitorForm(ModelForm):
    class Meta:
        model = Visitor
        fields = ['name','password']
        widgets = {
           
             'name' : forms.TextInput(attrs={'class':'form-control ','id':'my_name'}) ,
             'password' : forms.TextInput(attrs={'class':'form-control','id':'my_pass'}) ,

         }