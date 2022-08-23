# blog app urls.py
from django.urls import path
from .import views


app_name = 'blog'

urlpatterns = [
	path('', views.Blog, name='blog'),
	path('publisheds/', views.PublishedPostsBlog, name='published-posts-blog'),
	path('drafts/', views.DraftPostsBlog, name='draft-posts-blog'),
	path('postdetail/<slug:slug>/<int:pk>/', views.PostDetail, name='post-detail'),
	path('sharepost/<int:post_id>/', views.SharePost, name='share-post'),
]


