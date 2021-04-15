from . import views
from django.urls import path
from django.contrib.auth.decorators import permission_required


urlpatterns = [
    path('', views.PostList.as_view(), name='blog'),
    path('<int:pk>/', views.PostDetail.as_view(), name='blog_detail'),
    path('post/', permission_required('user.is_authenticated')(views.AddBlog.as_view()), name='add_blog')
]