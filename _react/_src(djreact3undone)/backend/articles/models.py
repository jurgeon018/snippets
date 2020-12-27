from django.db import models
from django.contrib import admin

class Article(models.Model):
    title = models.CharField(max_length=120)
    content = models.TextField()
    def __str__(self):
        return self.title
admin.site.register(Article)