from django.shortcuts import render, redirect
from .models import Post 
from django.contrib.auth.decorators import login_required
from . import forms 
# Create your views here.


def posts_list(request):
    posts = Post.objects.all().order_by('-date') # posts data
    return render(request, 'posts/posts_list.html', {'posts': posts}) # passing data onto the template

def post_page(request, slug):
    post = Post.objects.get(slug=slug) # post data
    return render(request, 'posts/post_page.html', {'post': post}) # passing data onto the template

@login_required(login_url="/users/login/") #checks if user is logged in else redirects them to login page
def post_new(request):
    if request.method == "POST": #send off the created post
        form = forms.CreatePost(request.POST, request.FILES)
        if form.is_valid():
            newPost = form.save(commit=False) # dosent save the posts instance object
            newPost.author = request.user
            newPost.save()
            return redirect('posts:list')
    else: # create new post
        form = forms.CreatePost()
    return render(request, 'posts/post_new.html', {'form': form})
