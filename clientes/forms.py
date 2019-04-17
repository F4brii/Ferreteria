from django import forms
from django.contrib.auth.models import User
from .models import Client

class LoginForm(forms.Form):
	username = forms.CharField(label='usuario:',max_length=15, widget=forms.TextInput(attrs={'class':'form-control'}))
	password = forms.CharField(label='contrasena', widget=forms.PasswordInput(attrs={'class':'form-control'}))

class UserForm(forms.ModelForm):
	class Meta:
		model = User 
		fields =[
			'username',
			'first_name',
			'last_name',
			'email',
			'password'
		]

class ContactForm(forms.Form):
	name = forms.CharField(label='Nombre', max_length=100)
	email = forms.CharField(label='Email', max_length=100)
	message = forms.CharField(label='Mensaje', widget=forms.Textarea)
	

