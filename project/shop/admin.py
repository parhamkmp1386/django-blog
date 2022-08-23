from django.contrib import admin
from .models import Product

# Register your models here.

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
	list_display = ('name', 'short_caption', 'mony','color',)
	list_display_links= ('short_caption',)
	list_editable = ('mony','name','color',)
	list_filter = ('status','publish','created','author',)
	search_fields = ('name','caption',)
	prepopulated_fields = {'slug':('name',)}
	raw_id_fields = ('author',)
	date_hierarchy = 'publish'
	ordering = ('status',)