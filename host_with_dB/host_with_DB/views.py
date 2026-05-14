from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'host_with_DB/index.html')

def idelete(request):
    return render(request, 'host_with_DB/delete_post.html')