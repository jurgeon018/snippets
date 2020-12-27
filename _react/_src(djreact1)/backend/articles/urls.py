from django.urls import path
from rest_framework.generics import ListAPIView, RetrieveAPIView
from django.db import models
from django.contrib import admin
from rest_framework import serializers

class Article(models.Model):
    title = models.CharField(max_length=120)
    content = models.TextField()
    def __str__(self):
        return self.title
admin.site.register(Article)

class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = ('id', 'title', 'content')

class ArticleListView(ListAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer

class ArticleDetailView(RetrieveAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer

urlpatterns = [
    path('', ArticleListView.as_view()),
    path('<pk>', ArticleDetailView.as_view()),
]

