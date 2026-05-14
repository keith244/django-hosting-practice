from django.shortcuts import render,get_object_or_404, redirect
from .models import Post

# Create your views here.
def index(request):
    posts = Post.objects.all()
    return render(request, 'host_with_DB/index.html',{'posts': posts})

def post_read(request,post_id):
    post = get_object_or_404(Post, id=post_id)
    return render(request, 'host_with_DB/post_read.html', {'post': post})

def post_delete(request,post_id):
    post = get_object_or_404(Post, id=post_id)
    post.delete()
    return redirect('index')