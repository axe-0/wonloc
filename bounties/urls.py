from django.urls import path, include 
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import ListView
from . import views
from hub import urls as hub_urls 
from .models import Bounty

app_name= "bounties"

urlpatterns =[

    path('music/',ListView.as_view(
        queryset = Bounty.objects.all(),
        template_name ="bounty.html"
    ), name="shortbounty"),
    path('hub/', include(hub_urls))
]

#ALLOWS templates to access and display images stored in your models.
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
