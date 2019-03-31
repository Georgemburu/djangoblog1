from django.shortcuts import render
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)
from .models import Post
from .forms import PostForm
# Create your views here.
class PostListView(ListView):
    model = Post
    def get_context_data(self, **kwargs):
         context = super().get_context_data()
         context['homeactive'] = True
         return context




class PostDetailView(DetailView):
    model = Post
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

class PostCreateView(CreateView):
    model = Post
    form_class = PostForm
   

class PostEditView(UpdateView):
    model = Post
    form_class = PostForm
    template_name_suffix = '_update_form'



class PostDeleteView(DeleteView):
    model = Post
    success_url = '../../'