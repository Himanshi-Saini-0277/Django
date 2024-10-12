from django.shortcuts import render, redirect
from .models import Post
from .forms import PostForm
from taggit.models import Tag
from .forms import TagFilterForm

def create_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('post_list')
    else:
        form = PostForm()
    return render(request, 'create_post.html', {'form': form})

def post_list(request):
    form = TagFilterForm(request.GET or None)
    if form.is_valid():
        tag_filter = form.cleaned_data.get('tag')
    else:
        tag_filter = ''

    if tag_filter:
        posts = Post.objects.filter(tags__name=tag_filter)
    else:
        posts = Post.objects.all()

    context = {
        'form': form,
        'posts': posts,
        'tags': Tag.objects.all(),
    }

    return render(request, 'post_list.html', context)
