from django.db import models

# Create your models here.
class Livros(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField()
    author = models.CharField(max_length=200)
    publishing_company =models.CharField(max_length=200)
    pages = models.IntegerField(upload_to='fotos/%d/%m/%Y', blank=True)
    