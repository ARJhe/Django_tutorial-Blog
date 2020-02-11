from django.shortcuts import render
from django.views.generic import ListView, DetailView

from django.http import HttpResponse
from .models import Post

# posts = [{
#     'author': 'JHE',
#     'title': 'Blog Post 1',
#     'content': 'First post content',
#     'date_posted': 'Jan 23, 2020'
# },
#     {'author': 'JHE',
#      'title': 'Blog Post 2',
#      'content': 'Second post content',
#      'date_posted': 'Jan 23, 2020'
#      },
# ]


def home(request):
    context = {
        'posts': Post.objects.all(),
    }
    return render(request, 'blog/home.html', context)

class PostListView(ListView):
    model = Post
    # from urls.py pathway PostListView.as_view() look forward a template
    # < app > / < model > _ < viewtpye >.html
    template_name = 'blog/home.html'
    # after named a template set variable and pass it to view
    context_object_name = 'posts'
    # order
    ordering = ['-date_posted']

class PostDetailView(DetailView):
    model = Post

def about(request):
    return render(request, 'blog/about.html', {'title': "About"})
