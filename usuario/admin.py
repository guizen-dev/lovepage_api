from django.contrib import admin
from .models import Usuario

# Register your models here.

class UsuarioAdmin(admin.ModelAdmin):
    list_display = ('user', 'password',)
    list_display_links = ('user',)
    list_per_page = 25


admin.site.register(Usuario, UsuarioAdmin)