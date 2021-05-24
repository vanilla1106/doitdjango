from django.shortcuts import render, redirect
from .models import Post, Category
from django.views.generic import ListView, DeleteView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

# Create your views here.
class PostList(ListView):
    model = Post
    ordering = '-pk'
    # template_name = 'blog/post_list.html'

    def get_context_data(self, **kwargs):
        context = super(PostList, self).get_context_data()
        context['categories'] = Category.objects.all()
        context['no_category_post_count'] = Post.objects.filter(category=None).count()
        return context

class PostDetail(DeleteView):
   model = Post

   def get_context_data(self, **kwargs):
        context = super(PostDetail, self).get_context_data()
        context['categories'] = Category.objects.all()
        context['no_category_post_count'] = Post.objects.filter(category=None).count()
        return context

def category_page(request, slug):
       if slug == 'no-category':
           category = '미분류'
           post_list = Post.objects.filter(category=None)
       else:
           category = Category.objects.get(slug=slug)
           post_list = Post.objects.filter(category=category)


       return render(
           request,
           'blog/post_list.html',
           {
               'post_list': post_list,
               'categories': Category.objects.all(),
               'no_category_post_count': Post.objects.filter(category=None).count(),
               'category': category,
           }
       )

class PostCreate(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    model = Post
    fields = ['title', 'hook_text', 'content', 'head_image', 'file_upload', 'category']

    def test_func(self):
        return self.request.user.is_superuser or self.request.user.is_staff

    def form_valid(self, form):
        current_user = self.request.user
        if current_user.is_authenticated and (current_user.is_staff or current_user.is_superuser):
            form.instance.author = current_user
            return super(PostCreate, self).form_valid(form)
        else:
            return redirect('/blog/')


