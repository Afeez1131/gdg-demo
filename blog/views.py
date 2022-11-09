from django.http import HttpResponse
from django.shortcuts import render
from .forms import BlogPostForm
from .models import BlogPost


def homepage(request):
    posts = BlogPost.objects.all()

    return render(request, 'blog/homepage.html', {'posts': posts})


def create_post(request):
    form = BlogPostForm()
    if request.method == 'POST':
        print(request.POST)
        form = BlogPostForm(request.POST)
        if form.is_valid():
            form.save()

    return render(request, 'blog/create_post.html', {'form': form})
