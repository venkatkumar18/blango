from django.shortcuts import render
from blog.models import Post, Comment, Tag
from django.utils import timezone
# Create your views here.

def index(request):
  posts = Post.objects.filter(published_at__lte=timezone.now())
 # print('\n\nPOST = {}\n\n'.format(posts))
  return render(request,'blog/index.html',{'posts':posts})

