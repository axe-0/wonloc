from django.contrib import admin
from .models import Thumbnail,Guild_status

# Register your models here.

@admin.register(Thumbnail)
class ThumbnailAdmin(admin.ModelAdmin):
    list_display=('thumbnail_id','image','category_text','status')


@admin.register(Guild_status)
class Guild_statusAdmin(admin.ModelAdmin):
    list_display = ('id','status')
