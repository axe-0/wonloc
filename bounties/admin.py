from django.contrib import admin
from .models import Bounty_category, Bounty, Fund, Apply

# Register your models here.

@admin.register(Bounty_category)
class Bounty_CategoryAdmin(admin.ModelAdmin):
    list_display= ('id','category')

@admin.register(Bounty)
class BountyAdmin(admin.ModelAdmin):
    list_display=('id','bounty_title','location','category_choice','despriction','overview','responsibilities','qualifications','inclosing','value')

@admin.register(Fund)
class FundAdmin(admin.ModelAdmin):
    list_display=('id','fund_title','bounty','intro','overview','why_support','how_to_help','qr_code')

@admin.register(Apply)
class ApplyAdmin(admin.ModelAdmin):
    list_display=('id','apply_title','bounty','intro','why_contribute',)


