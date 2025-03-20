from django import forms
from .models import Admission

class AdmissionForm(forms.ModelForm):
    class Meta:
        model = Admission
        fields = '__all__'  # Include all fields from the model
        widgets = {
            'name': forms.TextInput(attrs={'class': 'input-field', 'placeholder': 'Full Name'}),
            'address': forms.Textarea(attrs={'class': 'input-field', 'placeholder': 'Your Address', 'rows': 3}),
            'student_mobile': forms.TextInput(attrs={'class': 'input-field', 'placeholder': 'Student Mobile Number'}),
            'parent_mobile': forms.TextInput(attrs={'class': 'input-field', 'placeholder': 'Parent Mobile Number'}),
            'email': forms.EmailInput(attrs={'class': 'input-field', 'placeholder': 'Email Address'}),
            'board': forms.Select(attrs={'class': 'input-field'}),
            'physics_mark': forms.NumberInput(attrs={'class': 'input-field', 'placeholder': 'Physics Marks'}),
            'chemistry_mark': forms.NumberInput(attrs={'class': 'input-field', 'placeholder': 'Chemistry Marks'}),
            'mathematics_mark': forms.NumberInput(attrs={'class': 'input-field', 'placeholder': 'Mathematics Marks'}),
            'pcm_percentage': forms.NumberInput(attrs={'class': 'input-field', 'placeholder': 'PCM Percentage'}),
            'higher_secondary_percentage': forms.NumberInput(attrs={'class': 'input-field', 'placeholder': 'Higher Secondary Percentage'}),
            'preference_1': forms.Select(attrs={'class': 'input-field'}),
            'preference_2': forms.Select(attrs={'class': 'input-field'}),
            'preference_3': forms.Select(attrs={'class': 'input-field'}),
        }
