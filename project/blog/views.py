from django.shortcuts import render, get_object_or_404, redirect, HttpResponse
from .models import Post
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# Create your views here.

def HomePage(request):
	return render(request, 'blog/home.html')

def Blog(request):
	return render(request, 'blog/blog.html')

def PublishedPostsBlog(request):
	postscount = Post.objects.all().filter(status='published').count()
	posts = Post.objects.all().filter(status='published')
	paginator = Paginator(posts, 2)
	page = request.GET.get('page')
	try:
		posts = paginator.page(page)
	except PageNotAnInteger:
		posts = paginator.page(1)
	except EmptyPage:
		posts = paginator.page(paginator.num_pages)
	return render(request, 'blog/publishedPosts.html', {'posts':posts, 'postscount':postscount})

def DraftPostsBlog(request):
	postscount = Post.objects.all().filter(status='draft').count()
	posts = Post.objects.all().filter(status='draft')
	paginator = Paginator(posts, 2)
	page = request.GET.get('page')
	try:
		posts = paginator.page(page)
	except PageNotAnInteger:
		posts = paginator.page(1)
	except EmptyPage:
		posts = paginator.page(paginator.num_pages)
	return render(request, 'blog/draftPosts.html', {'posts':posts, 'postscount':postscount})


def PostDetail(request, post, pk):
	post=get_object_or_404(Post,slug=post,id=pk)
	return render(request, 'blog/postsdetail.html', {'post':post})
