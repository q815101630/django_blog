from django.shortcuts import render, get_object_or_404
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post
# posts = [
#     {
#         "author": "Megumi",
#         "title": "Nihao",
#         "content": "First post",
#         "date_posted": "August, 2055"
#     } 
# ]

def home(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, "django_blog/index.html", context=context)

class PostListView(ListView):
    model = Post
    template_name = 'django_blog/index.html'  #specify the tempalte_name:  app/model_viewtype.html
    context_object_name = "posts"
    ordering = ["-date_posted"]
    paginate_by = 5
    
class UserPostListView(ListView):
    model = Post
    template_name = 'django_blog/user_posts.html'  #specify the tempalte_name:  app/model_viewtype.html
    context_object_name = "posts"
    paginate_by = 5
    
    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Post.objects.filter(author=user).order_by("-date_posted")
        

    
class PostDetailView(DetailView):
    model = Post

class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'content']
    
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, CreateView):  #automatically use the same tempalte as CreateView
    model = Post
    fields = ['title', 'content']
    
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        else:
            return False

class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = "/"
    
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        else:
            return False
        
    

def about(request):
    return render(request, "django_blog/about.html")
