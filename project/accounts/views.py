from django.shortcuts import render, redirect
from .forms import AccountForm, ContactUsForm
from .models import Account
from django.core.mail import send_mail

def AccoutnPage(request):
	account = Account.objects.get(user=request.user)
	return render(request, 'accounts/index/accounts.html', {'account':account})

def SignUp(request):
	user = request.user
	try:
		account = Account.objects.get(user=user)
	except:
		account = Account.objects.create(user=user)
	if request.method == "POST":
		form=AccountForm(request.POST)
		if form.is_valid():
			user.first_name = form.cleaned_data['name']
			user.last_name = form.cleaned_data['lastname']
			account.gender = form.cleaned_data['gender']
			account.address = form.cleaned_data['address']
			account.age = form.cleaned_data['age']
			account.phone = form.cleaned_data['phone']
			user.save()
			account.save()
			return redirect('/')
			
		else:
			return render(request, 'accounts/forms/signup.html', {'form':form, 'account':account})
	form = AccountForm()
	return render(request, 'accounts/forms/signup.html', {'form':form, 'account':account})


def ContactUs(request):
	sent = False
	if request.method == "POST":
		form = ContactUsForm(request.POST)
		if form.is_valid():
			cd = form.cleaned_data
			subject = cd['subject']
			name = cd['name']
			phone = cd['phone']
			message = cd['message']
			email = cd['email']
			messgae_edit = f'name: {name}\nphone: {phone}\nemail: {email}\nsubject: {subject}\nmessage:\n{message}'
			send_mail(subject, messgae_edit, 'p1386karimipoor@gmail.com', ['parhamkarimipoor1386@gmail.com'], fail_silently=False)
			sent = True
	else:
		form = ContactUsForm()

	return render(request, 'accounts/forms/contactus.html', {'form':form,'sent':sent})



