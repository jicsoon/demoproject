from django import forms
from .models import Todo

# class TodoForm(forms.Form):
#     index = forms.IntegerField(widget=forms.NumberInput(attrs={'class':'form-control','placeholder':'Index Number'}))
#     content = forms.CharField(max_length=150,widget= forms.TextInput(attrs={'class':'form-control','placeholder':'Enter Todo Item'}))

class ModelTodoForm(forms.ModelForm):
    class Meta:
        model = Todo
        fields = ['tid','content']
        widgets = {
            'tid': forms.NumberInput(attrs={'class':'form-control','placeholder':'Index Number'}),
            'content' : forms.TextInput(attrs={'class':'form-control','placeholder':'Enter Todo Item'}) 
        }


