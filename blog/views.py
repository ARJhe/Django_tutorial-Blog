from django.contrib.auth.mixins import LoginRequiredMixin as lgmxin
from django.contrib.auth.mixins import UserPassesTestMixin as utpmxin
from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.views.generic import CreateView, DeleteView, UpdateView
from django.urls import reverse
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


def about(request):
    return render(request, 'blog/about.html', {'title': "About"})


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


# include lgmxin prevent unlog-in state access post/new/ route
class PostCreateView(lgmxin, CreateView):
    model = Post
    fields = ['title', 'content']

    # In order to fetch current author_id,
    # we have to overwrite method: form_valid()
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    # After finishing post creates
    # To let view handle redirect we use reverse to
    # return full url string to route
    def get_success_url(self):
        # give name_space registered in urls.py
        # which reverse will redirect after POST succeed
        return reverse('blog_home')


# include utpmxin prevent other user edit your post
class PostUpdateView(lgmxin, utpmxin, UpdateView):
    model = Post
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    # no auth no update
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return 1
        return 0

    def get_success_url(self):
        return reverse('blog_home')


class PostDeleteView(lgmxin, utpmxin, DeleteView):
    model = Post
    success_url = '/'
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    # no auth no delete
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return 1
        return 0

