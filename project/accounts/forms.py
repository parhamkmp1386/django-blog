from django import forms
from .models import Account

class AccountForm(forms.Form):
	GENDER_CHOICES=(
		('male', 'Male'),
		('fmale', 'Fmale'),
	)

	name = forms.CharField(max_length=25)
	lastname = forms.CharField(max_length=50)
	phone = forms.CharField(max_length=11, required=True)
	gender = forms.ChoiceField(choices=GENDER_CHOICES)
	address = forms.CharField(max_length=250)
	age = forms.IntegerField(required=True)

	def clean_phone(self):
		phone = self.cleaned_data['phone']
		if phone:
			if not phone.isnumeric():
				raise forms.ValidationError('The number must be a numeric character')
			else:
				return phone


	def clean_age(self):
		age = self.cleaned_data['age']
		if age:
			if age<0:
				raise forms.ValidationError('Age should not be 0 and should not be negative')
			else:
				return age


class ContactUsForm(forms.Form):
	message = forms.CharField(widget=forms.Textarea, required=True, label='Message')
	name = forms.CharField(max_length=50, required=True, label='Name And LastName')
	email = forms.EmailField(required=True, label='Email')
	subject = forms.CharField(required=True, max_length=50, label='Subject')
	phone = forms.CharField(max_length=11, required=True, label='Phone Number')

