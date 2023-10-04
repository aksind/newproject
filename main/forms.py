from django import forms
from .models import User1
class StudentRegistration(forms.ModelForm):
    class Meta:
        model=User1
        fields=['name','email','password']
        widgets={
            'name':forms.TextInput(attrs={'placeholder': 'Enter your name', 'style': 'width: 300px;','class':'form_control'}),
            'email':forms.TextInput(attrs={'placeholder': 'Enter your email', 'style': 'width: 300px;','class':'form_contol'}),
            'password':forms.PasswordInput(render_value=True,attrs={'placeholder': 'Enter your password', 'style': 'width: 300px;','class':'form_control'})   
        }