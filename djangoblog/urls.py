"""djangoblog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from .custom_site import custom_site
from django.urls import path, re_path
from Student.views import index, IndexView
from blog.views import has_perm, post_list, post_detail
from config.views import links
urlpatterns = [
    path('super_admin/', admin.site.urls),
    path('admin/', custom_site.urls),
    path(r'', index, name='index'),
    path(r'has_perm/', has_perm, name='has_perm'),
    path(r'web/', IndexView.as_view(), name='indexView'),
    re_path(r'category/(?P<category_id>\d+)', post_list, name='category'),
    path(r'index/', post_list, name='index/'),
    re_path(r'tag/(?P<tag_id>\d+)', post_list, name='tag'),
    path(r'links/', links, name='links'),
    re_path(r'post/(?P<post_id>\d+).html', post_detail, name='post'),
]
