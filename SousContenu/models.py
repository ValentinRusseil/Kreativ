from django.db import models
from Article.models import Article

# Create your models here.
class SousContenu(models.Model):
    sous_titre = models.CharField(max_length=100, verbose_name="sous titre", null=True, blank=True)
    sous_contenu = models.CharField(max_length=1000, verbose_name="Sous contenu")
    article = models.ForeignKey(Article, on_delete=models.CASCADE)