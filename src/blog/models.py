from django.db import models

# Create your models here.

class Blogpost(models.Model):
    # id = models.IntegerField()
    title  = models.TextField()
    slug   = models.SlugField(unique=True) 
    content = models.TextField(null=True, blank=True)

