from .models import Arequest
from django import forms



class CreateRequestForm(forms.ModelForm):
    class Meta:
        model = Arequest
        fields = '__all__'
        exclude = ['author', 'reqForDonate','type']

class CreateRequestForm2(forms.ModelForm):
    class Meta:
        model = Arequest
        fields = '__all__'
        exclude = ['author', 'reqForDonate']