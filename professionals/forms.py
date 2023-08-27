from django import forms
from .models import Profs

class ProfForm(forms.ModelForm):
    class Meta:
        model = Profs
        fields= ('occupation','name','title','institution','profile_pic','telephone',)