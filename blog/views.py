from django.shortcuts import render
from .models import Post, Category
from django.views.generic import ListView, DeleteView

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

# def index(request):
#     posts = Post.objects.all().order_by('-pk')
#
#     return render(
#         request,
#         'blog/post_list.html',
#         {
#             'posts': posts,
#         }
#     )

# def single_post_page(request, pk):
#     post = Post.objects.get(pk=pk)
#
#     return render(
#         request,
#         'blog/post_confirm_delete.html',
#         {
#             'post': post,
#         }
#     )