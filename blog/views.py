from django.shortcuts import render,get_object_or_404
from blog.models import Post, Comment, Tag
from django.utils import timezone
# Create your views here.

def index(request):
  posts = Post.objects.filter(published_at__lte=timezone.now())
 # print('\n\nPOST = {}\n\n'.format(posts))
  return render(request,'blog/index.html',{'posts':posts})

def post_detail(request,slug):
  post = get_object_or_404(Post,slug=slug)
  return render(request,"blog/post-detail.html",{"post":post})
