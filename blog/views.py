from django.shortcuts import render
from .models import Post
from django.views.generic import ListView, DeleteView

# Create your views here.
class PostList(ListView):
    model = Post
    ordering = '-pk'
    # template_name = 'blog/post_list.html'

class PostDetail(DeleteView):
    model = Post


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