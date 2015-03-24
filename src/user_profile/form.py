from django import forms

class ProfileForm(forms.Form):
	email = forms.CharField(widget=forms.EmailInput(attrs={
		'class' : 'form-control',
		'placeholder' : 'Email',
		'type' : 'email'
	}))

	