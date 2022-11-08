from django.urls import path

from blog.api_views import post_list, post_detail

urlpatterns = [
  path('post/',post_list,name='api_post_list'),
  path('post/<int:pk>',post_detail,name='api_post_detail')

]