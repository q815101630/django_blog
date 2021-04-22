from django.shortcuts import render
from django.http import HttpResponse
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

def about(request):
    return render(request, "django_blog/about.html")
