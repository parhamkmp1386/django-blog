from django.contrib import admin
from .models import Post, Comment
# Register your models here.

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
	list_display = ('title', 'short_body', 'status',)
	list_display_links= ('short_body',)
	list_editable = ('status','title',)
	list_filter = ('status','publish','created','author',)
	search_fields = ('title','body',)
	prepopulated_fields = {'slug':('title',)}
	raw_id_fields = ('author',)
	date_hierarchy = 'publish'
	ordering = ('status',)


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
	list_display = ('name', 'post', 'active',)
	list_display_links = ('name',)
	list_editable = ('active',)
	list_filter = ('active', 'post', 'name')
	search_fields = ('name',)
