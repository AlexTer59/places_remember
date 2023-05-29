from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)
from .models import Post
import folium


def home(request):
    context = {
        'posts': Post.objects.filter(author=request.user).order_by('-date_posted')
        # Post.objects.filter(author=request.user).order_by('-date_posted')  Посты авторизированного пользователя
        # чтобы видеть все: Post.objects.all
    }
    # чтобы видеть все: Post.objects.all
    return render(request, 'blog/home.html', context)


class PostListView(ListView):
    model = Post
    template_name = 'blog/home.html'
    context_object_name = 'posts'
    ordering = ['-date_posted']


class PostDetailView(DetailView):
    model = Post

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        m = folium.Map(location=[56.8519, 60.6122], zoom_start=12)
        m = m._repr_html_()
        ctx['m'] = m
        return ctx

class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        m = folium.Map(location=[56.8519, 60.6122], zoom_start=12)
        m = m._repr_html_()
        ctx['m'] = m
        return ctx


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        m = folium.Map(location=[56.8519, 60.6122], zoom_start=12)
        m = m._repr_html_()
        ctx['m'] = m
        return ctx

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = '/home'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


def about(request):
    return render(request, 'blog/about.html', {'title': 'Places Remember'})
