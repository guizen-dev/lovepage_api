from django.contrib import admin

# Register your models here.

from django.contrib import admin
from .models import Reclamacao, ChatReclamacao

# Register your models here.

class ReclamacaoAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'state', 'user')
    list_display_links = ('title',)
    list_per_page = 25

class ChatReclamacaoAdmin(admin.ModelAdmin):
    list_display = ('reclamacao', 'isEnvio', 'user', 'desc')
    list_display_links = ('reclamacao',)
    list_per_page = 25

admin.site.register(Reclamacao,ReclamacaoAdmin)
admin.site.register(ChatReclamacao,ChatReclamacaoAdmin)
