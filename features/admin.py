from django.contrib import admin
from .models import Feature

# Register your models here.

class FeatureAdmin(admin.ModelAdmin):
    list_display = ('name',)
    list_display_links = ('name',)
    list_per_page = 25

admin.site.register(Feature,FeatureAdmin)