from django.shortcuts import render,get_object_or_404, redirect
from django.http import HttpResponse
from django.core import cache
from .models import Post

# Create your views here.
def index(request):
    posts = Post.objects.all()
    return render(request, 'host_with_DB/index.html',{'posts': posts})

def create_post(request):
    ip = request.META.get('REMOTE_ADDR')

    # rate limit key
    cache_key = f"create_post_{ip}"

    #check if user posted recently
    if cache.get(cache_key):
        return HttpResponse("Too many requests. Please wiat before creating another post.", status=429)
    if request.method == 'POST':
        title = request.POST.get('title')
        content = request.POST.get('content')
        Post.objects.create(title=title, content=content)
        # set rate limit for 1 minute
        cache.set(cache_key, True, timeout=60)
        return redirect('index')
    return render(request, 'host_with_DB/create_post.html') 

def post_read(request,post_id):
    post = get_object_or_404(Post, id=post_id)
    return render(request, 'host_with_DB/post_read.html', {'post': post})

def post_delete(request,post_id):
    post = get_object_or_404(Post, id=post_id)
    post.delete()
    return redirect('index')