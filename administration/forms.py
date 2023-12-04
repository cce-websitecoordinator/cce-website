from django import forms
from .models import *

class GrievanceBodyForm(forms.ModelForm):
    class Meta:
        model = GrievanceBody
        fields = ['name', 'email', 'type', 'category', 'subject', 'message']

    def __init__(self, *args, **kwargs):
        super(GrievanceBodyForm, self).__init__(*args, **kwargs)

        # Make 'name' and 'email' fields non-editable
        self.fields['name'].widget.attrs['readonly'] = True
        self.fields['email'].widget.attrs['readonly'] = True
        self.fields['type'].widget.attrs['readonly'] = True