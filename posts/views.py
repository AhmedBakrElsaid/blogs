from django.shortcuts import render,redirect
from django.urls import reverse
from .models import Post
from .forms import PostForm
# Create your views here.

def post_list(request):
    
    objects = Post.objects.all()
    return render(request,'posts/posts.html',{'posts':objects})

def post_detail (request,id):
    single = Post.objects.get(id = id)
    return render (request,'posts/detail.html',{'post': single})

def new_post (request):
    if request.method == "POST":
      form = PostForm(request.POST,request.FILES)
      if form.is_valid():
        myform=form.save(commit=False)
        myform.author = request.user
        myform.save()
        return redirect(reverse('blogs:post_list'))
          
    else:
        print("in else")
        form = PostForm()
    return render(request,'posts/forms.html',{'new':form})

def edit_post (request,id):
    single = Post.objects.get(id = id)
    if request.method == "POST":
      form = PostForm(request.POST,request.FILES,instance=single)
      if form.is_valid():
          form.save()
    else:
        print("in else")
        form = PostForm(instance=single)
    return render(request,'posts/edit.html',{'new':form})


def post_delete (request,id):
    single = Post.objects.get(id = id)
    single.delete()
    return redirect(reverse('blogs:post_list'))

