from django.urls import path
from .import views

app_name = 'accounts'

urlpatterns = [
	path('', views.AccoutnPage, name='user-account'),
	path('signup/', views.SignUp, name='signup-account'),
	path('contactus/', views.ContactUs, name='contactus-account'),
	# path('login/', views., name='login-account'),
]

