from django.views import generic
from .models import Post
from django.core.mail import send_mail

class PostList(generic.ListView):
    model = Post
    template_name = 'index.html'

class PostDetail(generic.DetailView):
    model = Post
    template_name = 'blog_detail.html'

class AddBlog(generic.CreateView):
    model = Post
    template_name = 'add_blog.html'
    fields = ['title','author', 'body','status']

