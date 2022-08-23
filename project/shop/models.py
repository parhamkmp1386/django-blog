from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.

class Product(models.Model):
	STATUS_CHOICES=(
		('not-have','Not Have'),
		('have', 'Have'),
	)
	MONY_CHOICES=(
		('$','$'),
		('تومان','تومان')
	)
	COLOR_CHOICES=(
		('select color please ...', 'select color please ...'),
		('red', 'red'),
		('blue', 'blue'),
		('yellow', 'yellow'),
		('black', 'black'),
		('white', 'white'),
	)
	name = models.CharField(max_length=250) 
	slug = models.SlugField(max_length=250,unique_for_date='publish')
	suk = models.CharField(max_length=10, null=False)
	author = models.ForeignKey(User,on_delete=models.CASCADE,related_name='product_posts')
	price = models.IntegerField() 
	color = models.CharField(choices=COLOR_CHOICES, max_length=250, default='select color please ...')
	caption = models.TextField()
	def short_caption(self):
		return self.caption[:50] + ' ..... '
	publish = models.DateTimeField(default=timezone.now)
	created = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)
	status = models.CharField(max_length=10,choices=STATUS_CHOICES,default='have')
	mony = models.CharField(max_length=10,choices=MONY_CHOICES,default='dollers')


	class Meta:
		ordering = ('-publish',)

	def get_absolute_url(self):
		return reverse('shop:product-detail',args=[self.slug, self.id])

	def __str__(self):
		priceStr = str(self.price)
		return self.name + '-' + priceStr + self.mony
