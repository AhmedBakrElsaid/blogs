from django.shortcuts import render
from .models import Post
from .forms import PostForm
# Create your views here.

def post_list(request):
    
    objects = Post.objects.all()
    return render(request,'posts.html',{'posts':objects})

def post_detail (request,id):
    single = Post.objects.get(id = id)
    return render (request,'detail.html',{'post': single})

def new_post (request):
    if request.method == "POST":
      form = PostForm(request.POST,request.FILES)
      if form.is_valid():
          form.save()
    else:
        print("in else")
        form = PostForm()
    return render(request,'forms.html',{'new':form})

def edit_post (request,id):
    single = Post.objects.get(id = id)
    if request.method == "POST":
      form = PostForm(request.POST,request.FILES,instance=single)
      if form.is_valid():
          form.save()
    else:
        print("in else")
        form = PostForm(instance=single)
    return render(request,'edit.html',{'new':form})