from turtle import title
from django.db import models
class meetup(models.Model):
    title= models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    description =models.TextField()