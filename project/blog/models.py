from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.

class Post(models.Model):
	 STATUS_CHOICES=(
	 	('draft','Draft'),
	 	('published', 'Published'),
	 )
	 title = models.CharField(max_length=250) 
	 slug = models.SlugField(max_length=250,unique_for_date='publish')
	 author = models.ForeignKey(User,on_delete=models.CASCADE,related_name='blog_posts')
	 body = models.TextField()
	 def short_body(self):
	 	return self.body[:30] + ' ..... '
	 publish = models.DateTimeField(default=timezone.now)
	 created = models.DateTimeField(auto_now_add=True)
	 updated = models.DateTimeField(auto_now=True)
	 status = models.CharField(max_length=10,choices=STATUS_CHOICES,default='draft')

	 class Meta:
	 	ordering = ('-publish',)


	 def get_absolute_url(self):
	 	return reverse('blog:post-detail',args=[self.slug, self.id])

	 def __str__(self):
	 	return 'title: (' + self.title + ')' + 'Body: ' + self.short_body()



class Comment(models.Model):
	post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
	name = models.CharField(max_length=100)
	body = models.TextField()
	created = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)
	active = models.BooleanField(default=False)

	class Meta:
		ordering = ('created',)

	def __str__(self):
		return f'Comment By{self.name} on {self.post}'