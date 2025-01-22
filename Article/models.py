from django.db import models

# Create your models here.
class Article(models.Model):
    titre = models.CharField(max_length=100, verbose_name="Titre")
    image = models.ImageField(max_length=128, null=True, blank=True, verbose_name="Image de l'article", upload_to='assets/')