from distutils.command.clean import clean
from django import forms

from django.contrib.auth.models import User

class RegisterForm(forms.Form):
    username = forms.CharField(label='Nombre de Usuario',
                               required=True,
                               min_length=4, max_length=50,
                               widget=forms.TextInput(attrs={
                                   'class': 'form-control',
                                   'id': 'username',
                                   'placeholder': 'Usuario'
                               })) 
    email = forms.EmailField(label='Correo electrónico',
                                required=True,
                                min_length=4, max_length=50,
                                widget=forms.EmailInput(attrs={
                                    'class': 'form-control',
                                    'id': 'email'
                                }))                                           
    password = forms.CharField(label='Contraseña',
                               required=True,
                               widget=forms.PasswordInput(attrs={
                                   'class': 'form-control'
                               }))
    
    password2 = forms.CharField(label='Confirmar Contraseña',
                                required=True,
                                widget=forms.PasswordInput(attrs={
                                    'class': 'form-control'
                                }))
    
    def clean_username(self):
        username = self.cleaned_data.get('username')
        
        if User.objects.filter(username=username).exists():
           raise forms.ValidationError('El usuario ya existe!')
        
        return username
    
    def clean_email(self):
        email = self.cleaned_data.get('email')
        
        if User.objects.filter(email=email).exists():
           raise forms.ValidationError('El email ya existe!')
        
        return email
    
    def clean(self):
        cleaned_data = super().clean()
        
        if cleaned_data.get('password2') != cleaned_data.get('password'):
            self.add_error('password2', 'La contraseña no es la misma')
    
    def save(self):
        return User.objects.create_user(
            self.cleaned_data.get('username'),
            self.cleaned_data.get('email'),
            self.cleaned_data.get('password'),
        )