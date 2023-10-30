from django.urls import path, include 
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import ListView
from . import views


app_name = 'hub'

urlpatterns = [
    path('music/',views.music_page , name= "music_hub" ),
    path('<int:bount_id>',views.bounty_details, name="bountydetails"),
    path('<int:apply_id>/apply',views.apply_bounty, name="bountyapply"),
    path('<int:fund_id>/fund',views.fund_bounty, name="bountyfund"),
    path('submission/',views.application_submission, name='submission'),
    path('like/<int:post_id>', views.toggle_like, name='toggle_like'),
    path('comment/<int:post_id>', views.comment_sub, name="save_comment"),
    
]

#ALLOWS templates to access and display images stored in your models.
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    