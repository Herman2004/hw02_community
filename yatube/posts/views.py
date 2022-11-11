from django.shortcuts import render, get_object_or_404
from posts.models import Group, Post


LAST_POSTS_QUANTITY = 10


def index(request):
    posts = Post.objects.all()[:LAST_POSTS_QUANTITY]
    context = {
        'posts': posts,
    }
    return render(request, 'posts/index.html', context)


def group_posts(request, slug):
    group = get_object_or_404(Group, slug=slug)
    posts = Post.objects.filter(group=group)[:LAST_POSTS_QUANTITY]
    context = {
        'group': group,
        'posts': posts,
    }
    return render(request, 'posts/group_list.html', context)
