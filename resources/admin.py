from django.contrib import admin
from .models import ResourceCategory, LibraryItem

# Register your models here.

@admin.register(ResourceCategory)
class ResourceCategoryAdmin(admin.ModelAdmin):
    list_display =('id','category')

@admin.register(LibraryItem)
class LibraryItemAdmin(admin.ModelAdmin):
    list_display =('id','title','file','category','image')
