from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from .forms import BlogPostForm
from .models import BlogPost


def homepage(request):
    posts = BlogPost.published.all()

    return render(request, 'blog/homepage.html', {'posts': posts})

@login_required
def create_post(request):
    form = BlogPostForm()
    if request.method == 'POST':
        print(request.POST)
        form = BlogPostForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('post_list'))

    return render(request, 'blog/create_post.html', {'form': form})


def update_post(request, bid):
    post = BlogPost.objects.get(id=bid)
    form = BlogPostForm(instance=post)
    if request.method == 'POST':
        form = BlogPostForm(instance=post, data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('post_list'))

    return render(request, 'blog/update_post.html', {'form': form})


def detail_post(request, slug):
    post = BlogPost.objects.get(slug=slug)

    return render(request, 'blog/post_detail.html', {'post': post})


"""
updating

--->>
Authorization - specifying right/privileges to resources
                deciding whether a user is allowed to perform an action.
Authentication - the process of verifying the identity of a user
"""
