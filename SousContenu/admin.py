from django.contrib import admin
from SousContenu.models import SousContenu

class SousContenuAdmin(admin.ModelAdmin):
    list_display = ('sous_titre', 'sous_contenu', 'article')

admin.site.register(SousContenu, SousContenuAdmin)
