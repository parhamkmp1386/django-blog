from django.shortcuts import render, get_object_or_404, redirect, HttpResponse
from .models import Post, Comment
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .forms import SharePostForm, CommentPostForm
from django.core.mail import send_mail
# from django.db.models import Count

# Create your views here.
def Blog(request):
	return render(request, 'blog/index/blog.html')

def PublishedPostsBlog(request):
	postscount = Post.objects.all().filter(status='published').count()
	posts = Post.objects.all().filter(status='published')
	paginator = Paginator(posts, 5)
	page = request.GET.get('page')
	try:
		posts = paginator.page(page)
	except PageNotAnInteger:
		posts = paginator.page(1)
	except EmptyPage:
		posts = paginator.page(paginator.num_pages)
	context = {
		'posts':posts, 
		'postscount':postscount,
	}
	return render(request, 'blog/post/publishedPosts.html', context)

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
	return render(request, 'blog/post/draftPosts.html', {'posts':posts, 'postscount':postscount})


def PostDetail(request, slug,pk):
	post=get_object_or_404(Post,slug=slug,id=pk)
	# comments = Comment.objects.filter(post=post, active=True) # 1
	comments = post.comments.filter(active=True) # 2
	new_comment = None
	if request.method == 'POST':
		form = CommentPostForm(request.POST)
		if form.is_valid():
			new_comment = form.save(commit=False)
			new_comment.post = post
			new_comment.save()
	else:
		form = CommentPostForm()

	context = {
		'post':post,
		'comments':comments,
		'new_comment':new_comment,
		'form':form,
		'comments_count':comments.count()
	}
	return render(request, 'blog/post/postsdetail.html', context)



def SharePost(request, post_id):
	sent=False
	post = get_object_or_404(Post, status='published', id=post_id)
	if request.method == "POST":
		form = SharePostForm(request.POST)
		if form.is_valid():
			cd = form.cleaned_data
			post_url = request.build_absolute_uri(post.get_absolute_url())
			name = cd['name']
			subject = f'{name} has invited you to read the {post.title}'
			message = cd['message']
			to = cd['to']
			msg = f'{name} invites you to read post {post.title} at the following address:\n{post_url}'
			send_mail(subject, msg, 'p1386karimipoor@gmail.com', [to], fail_silently=False)
			sent = True
	else:
		form = SharePostForm()

	return render(request, 'blog/post/sharePost.html', {'form':form,'sent':sent, 'post':post})




# def CommentPost

