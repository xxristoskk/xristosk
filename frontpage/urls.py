from django.contrib import admin
from django.urls import path, include
from .views import ContactView, datasets, projects
from blog.views import PostList

urlpatterns = [
    path('', ContactView.as_view(), name='home'),
    path('blog/', PostList.as_view(), name='blog'),
    path('datasets/', datasets, name='datasets'),
    path('projects/', projects, name='projects')
]
