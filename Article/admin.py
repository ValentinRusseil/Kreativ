from django.contrib import admin
from Article.models import Article
from SousContenu.models import SousContenu

class SousContenuInline(admin.TabularInline):
    model = SousContenu
    extra = 1  # Nombre de lignes vides supplémentaires pour ajouter de nouveaux sous-contenus
    fields = ('sous_titre', 'sous_contenu')  # Champs à afficher dans l'inline

class ArticleAdmin(admin.ModelAdmin):
    list_display = ('titre', 'image',)
    inlines = [SousContenuInline]

admin.site.register(Article, ArticleAdmin)
