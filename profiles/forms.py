
from .models import Aprofile
from django import forms


class EditProfileForm(forms.ModelForm):
    class Meta:
        model = Aprofile
        fields = '__all__'
        exclude = ['user']

