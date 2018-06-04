# -*- coding: utf-8 -*-
from django import forms
from django.core.validators import RegexValidator
 

class PasswordResetFormCustom(forms.Form):
    
    dni = forms.CharField(label='DNI',
                          required=True,
                          max_length=15, 
                          validators=[RegexValidator(r'^\d{1,10}$')],
                          widget=forms.TextInput(attrs={'class':'form-control'}))
    username = forms.CharField(label='Usuario',
                               required=True,
                               max_length=15, 
                               widget=forms.TextInput(attrs={'class':'form-control'}))
                               