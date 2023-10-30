from django.shortcuts import render
from .models import Thumbnail
from django.shortcuts import render, get_object_or_404,redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse


# Create your views here.

def index(request):
    return render(request, 'launch.html')


def thumb_link(request, thumbnail_id):
    '''get thumbnail category and redirect
      to the appropriate page hub ie music hub
    '''
    thumbnail = get_object_or_404(Thumbnail,pk=thumbnail_id)
    thumb_cat = thumbnail.category_text.lower()

    if thumb_cat == "music":
        return HttpResponseRedirect(reverse('hub:music_hub'))
    else:
        context ={
            'thumb_cat': thumb_cat,
        }
        return render(request, 'comingsoon.html', context)
    
