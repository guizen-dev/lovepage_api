from django.contrib import admin
from .models import Lugar, Mural, Jogo, Filme

# Register your models here.

class LugarAdmin(admin.ModelAdmin):
    list_display = ('name',)
    list_display_links = ('name',)
    list_per_page = 25

class MuralAdmin(admin.ModelAdmin):
    list_display = ('name',)
    list_display_links = ('name',)
    list_per_page = 25

class JogoAdmin(admin.ModelAdmin):
    list_display = ('name',)
    list_display_links = ('name',)
    list_per_page = 25

class FilmeAdmin(admin.ModelAdmin):
    list_display = ('name',)
    list_display_links = ('name',)
    list_per_page = 25

admin.site.register(Lugar,LugarAdmin)
admin.site.register(Mural,MuralAdmin)
admin.site.register(Jogo,JogoAdmin)
admin.site.register(Filme,FilmeAdmin)