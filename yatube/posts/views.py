from django.shortcuts import render, get_object_or_404
from .models import Group, Post


last_posts_quantity = 10


def index(request):
    template = 'posts/index.html'
    posts = Post.objects.order_by('-pub_date')[:last_posts_quantity]
    context = {
        'posts': posts,
    }
    return render(request, template, context=context)


def group_posts(request, slug):
    template = 'posts/group_list'
    group = get_object_or_404(Group, slug)
    posts = Post.objects.filter(group=group).order_by(
        '-pub_date'
    )[:last_posts_quantity]
    context = {
        'group': group,
        'posts': posts
    }
    return render(request, template, context)
