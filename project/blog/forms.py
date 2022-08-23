from django import forms
from .models import Comment

class SharePostForm(forms.Form):
	message = forms.CharField(widget=forms.Textarea, required=True, label='Message')
	name = forms.CharField(max_length=50, required=True, label='Name And LastName')
	to = forms.EmailField(required=True, label='Email')


class CommentPostForm(forms.ModelForm):
	class Meta:
		model = Comment
		fields = ('name', 'body')

