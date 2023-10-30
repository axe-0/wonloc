from django.contrib import admin
from .models import Guild,Type,Category,Post,Comment

# Register your models here.

@admin.register(Guild)
class GuildAdmin(admin.ModelAdmin):
    list_display =('id','guild')

@admin.register(Type)
class TypeAdmin(admin.ModelAdmin):
    list_display =('id','title')

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display =('id','category')

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display =('id','user','guild','title','content','created_at','type','category')

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display =('id','user','post','content','created_at')