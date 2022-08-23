from django.contrib import admin
from .models import Account

# Register your models here.

@admin.register(Account)
class AccountAdmin(admin.ModelAdmin):
	list_display = ('user', 'gender')
	list_display_links = ('user',)