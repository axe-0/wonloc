from django.urls import path, include 
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import ListView
from . import views

app_name = 'library'

urlpatterns = [

]

#ALLOWS templates to access and display images stored in your models.
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)