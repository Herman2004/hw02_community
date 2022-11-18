from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404
from posts.models import Group, Post, User


POSTS_QUANTITY_IN_PAGINATOR = 10


def index(request):
    post_list = Post.objects.all()
    paginator = Paginator(post_list, POSTS_QUANTITY_IN_PAGINATOR)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'page_obj': page_obj,
    }
    return render(request, 'posts/index.html', context)


LAST_POSTS_QUANTITY = 10
def group_posts(request, slug):
    group = get_object_or_404(Group, slug=slug)
    posts = Post.objects.filter(group=group)[:LAST_POSTS_QUANTITY]
    context = {
        'group': group,
        'posts': posts,
    }
    return render(request, 'posts/group_list.html', context)


def profile(request, username):
    # Здесь код запроса к модели и создание словаря контекста
    the_user = get_object_or_404(User, username=username)
    post_list = Post.objects.filter(author=the_user)
    paginator = Paginator(post_list, POSTS_QUANTITY_IN_PAGINATOR)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    posts_quantity = Post.objects.filter(author=the_user).count()
    context = {
        'page_obj': page_obj,
        'User': the_user,
        'posts_quantity': posts_quantity
    }
    return render(request, 'posts/profile.html', context)


def post_detail(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    posts_quantity = Post.objects.filter(author=post.author).count()
    context = {
        'post': post,
        'posts_quantity': posts_quantity
    }
    return render(request, 'posts/post_detail.html', context)