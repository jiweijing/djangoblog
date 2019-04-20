from django.shortcuts import render
from django.http.response import HttpResponse
from django.views import View
from django.views.generic import DetailView, ListView
from django.shortcuts import get_object_or_404
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


class MyView(View):
    
    def get(self, request):
        return HttpResponse('resault')


class CommonViewMixin:
    """ 创建Mixin 进行数据的 上下文 """
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            'sidebars': SideBar.get_all()
        })
        return context


class PostListView(CommonViewMixin, ListView):
    queryset = Post.latest_posts()
    paginate_by = 5
    context_object_name = 'post_list'
    template_name = 'list1.html'


class PostDetailView(CommonViewMixin, DetailView):
    model = Post
    template_name = 'detail1.html'
    context_object_name = 'post'
    pk_url_kwarg = 'post_id'


class CategoryView(PostListView):
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        category_id = self.kwargs.get('category_id')
        category = get_object_or_404(Category, pk=category_id)
        context.update({
            'category': category
        })
        return context
    
    def get_queryset(self):
        """ 重写 querset 根据分类过滤 """
        queryset = super().get_queryset()
        category_id = self.kwargs.get('category_id')
        return queryset.filter(category_id=category_id)


class TagView(PostListView):
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        tag_id = self.kwargs.get('tag_id')
        tag = get_object_or_404(Tag, pk=tag_id)
        context.update({
            'tag': tag
        })
        return context
    
    def get_queryset(self):
        """ 重写 querset 根据分类过滤 """
        queryset = super().get_queryset()
        tag_id = self.kwargs.get('tag_id')
        return queryset.filter(tag_id=tag_id)


