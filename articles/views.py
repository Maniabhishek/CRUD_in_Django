from django.shortcuts import render
from django.views.generic import ListView , DetailView ,CreateView ,UpdateView , DeleteView
from .models import Article

from django.urls import reverse_lazy
# Create your views here.
class ArticleListView(ListView):
    model = Article
    template_name = 'home.html'
    context_object_name = 'my_favorite_publishers'


class ArticleDetailView(DetailView):
    model = Article
    template_name = 'detail.html'
    context_object_name = 'detailv'

class ArticleCreateView(CreateView):
    model = Article
    template_name = 'article_new.html'
    fields = '__all__'


class ArticleUpdateView(UpdateView):
    model = Article
    template_name = 'edit.html'
    fields = ['title','text']

class ArticleDeleteView(DeleteView):
    model = Article
    template_name = 'delete.html'
    context_object_name = 'bat'
    success_url = reverse_lazy('home')
    




    