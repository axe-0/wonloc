from django.urls import path, include 
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import ListView, DetailView
from . import views
from .models import Thumbnail

app_name = "dashboard"

urlpatterns =[
    path('',views.index, name="landing"),
    path('discover/',ListView.as_view(
        queryset= Thumbnail.objects.all(),
        template_name ="thumbnails.html"
        
    ),name= "discover",),
    path('<int:thumbnail_id>/',views.thumb_link, name="guildpage"),
]

#ALLOWS templates to access and display images stored in your models.
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
