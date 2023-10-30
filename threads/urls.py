from django.urls import path, include 
from django.views.generic import ListView
from .models import Post
from . import views
from hub import urls as hub_urls 


app_name = 'threads'

urlpatterns = [
    path('music/',ListView.as_view(
        queryset = Post.objects.all(),
        template_name ="threads_list.html"
    ),name="threadlist"),
   
]