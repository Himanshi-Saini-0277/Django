from django import forms
from .models import Post
from taggit.models import Tag

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content', 'tags']

class TagFilterForm(forms.Form):
    tag = forms.ModelChoiceField(
        queryset = Tag.objects.all(),
        required = False,
        label = "Filter by tag"
    )