from django.shortcuts import render

from .models import Post

def home(request):
	return render(request, 'home.html')

def list(request):
	posts = Post.objects.all().order_by('-date')
	return render(request, 'blog/list.html', {'posts': posts})