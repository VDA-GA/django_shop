from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, ListView, UpdateView, DeleteView

from blog.models import Blog


class BlogCreateView(CreateView):
    model = Blog
    fields = ('title', 'slug', 'body', 'picture',)
    success_url = reverse_lazy('blog:list')


class BlogListView(ListView):
    model = Blog


class BlogDetailView(DetailView):
    model = Blog


class BlogUpdateView(UpdateView):
    model = Blog
    fields = ('title', 'slug', 'body', 'picture',)
    success_url = reverse_lazy('blog:list')


class BlogDeleteView(DeleteView):
    model = Blog
    success_url = reverse_lazy('blog:list')
