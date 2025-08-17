# blog/forms.py
from django import forms
from .models import Post
from .models import Comment
from taggit.forms import TagWidget  # <-- import TagWidget

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ["title", "content"]
        widgets = {
            'tags': TagWidget(),  # <-- add the TagWidget here
        }


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['title', 'content', 'tags']
        widgets = {
            'content': forms.Textarea(attrs={'rows': 3, 'placeholder': 'Write a comment...'}),
        }