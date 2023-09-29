from django import forms
from .models import *

class GrievanceBodyForm(forms.ModelForm):
    class Meta:
        model = GrievanceBody
        fields = '__all__'