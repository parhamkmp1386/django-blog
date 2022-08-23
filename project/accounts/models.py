from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Account(models.Model):
	GENDER_CHOICES=(
		('male', 'Male'),
		('fmale', 'Fmale'),
	)
	user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='account')
	gender = models.CharField(max_length=5, choices=GENDER_CHOICES, default='male')
	phone = models.CharField(max_length=11, null=True, blank=True)
	address = models.TextField(null=True, blank=True)
	created = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)
	age = models.PositiveIntegerField(default=0)

	def __str__(self):
		return self.user.first_name +" "+ self.user.last_name
