from django.shortcuts import render
from django.http.response import HttpResponse
from .models import Tag, Post, Category
from config.models import SideBar


# Create your views here.
def has_perm(request):
    return HttpResponse(status=200)


def post_list(request, tag_id=None, category_id=None, *args, **kwargs):
    tag = None
    category = None
    if tag_id:
        post_list, tag = Post.get_by_tag(tag_id)
    elif category_id:
        post_list, category = Post.get_by_category(category_id)
    else:
        post_list = Post.latest_posts()
    context = {
        'category': category,
        'tag': tag,
        'post_list': post_list,
        'sidebars': SideBar.get_all()
    }
    context.update(Category.get_navs())
    return render(request, 'list.html', context=context)


def post_detail(request, post_id=None, *args, **kwargs):
    try:
        post = Post.objects.get(id=post_id)
    except Post.DoesNotExist:
        post = None
    context = {
        'post': post,
        'sidebars': SideBar.get_all()
    }
    context.update(Category.get_navs())
    return render(request, 'detail.html', context=context)
