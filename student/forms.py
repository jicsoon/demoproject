from django.forms import ModelForm
from .models import Student
from django import forms

class StudentForm(ModelForm):
    class Meta:
        model = Student
        fields = ['sid','name','grad_date','score']
        widgets = {
             'sid': forms.NumberInput(attrs={'class':'form-control'}),
             'name' : forms.TextInput(attrs={'class':'form-control',}) ,
             'grad_date' : forms.TextInput(attrs={'class':'form-control','placeholder':'YYYY-MM-DD'}) ,   
             'score' : forms.NumberInput(attrs={'class':'form-control'}) 

         }

         