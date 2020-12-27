from django.urls import path
from .models import *
from rest_framework import serializers

class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = ('id', 'title', 'content')


# from rest_framework.generics import (
#     ListAPIView, RetrieveAPIView, CreateAPIView, DestroyAPIView,
#     UpdateAPIView, )

# class ArticleListView(ListAPIView):
#     queryset = Article.objects.all()
#     serializer_class = ArticleSerializer

# class ArticleDetailView(RetrieveAPIView):
#     queryset = Article.objects.all()
#     serializer_class = ArticleSerializer

# class ArticleCreateView(CreateAPIView):
#     queryset = Article.objects.all()
#     serializer_class = ArticleSerializer

# class ArticleDeleteView(DestroyAPIView):
#     queryset = Article.objects.all()
#     serializer_class = ArticleSerializer

# class ArticleUpdateView(UpdateAPIView):
#     queryset = Article.objects.all()
#     serializer_class = ArticleSerializer

# urlpatterns = [
#     path('', ArticleListView.as_view()),
#     path('create/', ArticleCreateView.as_view()),
#     path('<pk>/delete/', ArticleDeleteView.as_view()),
#     path('<pk>/update/', ArticleUpdateView.as_view()),
#     path('<pk>', ArticleDetailView.as_view()),

# ]

# # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# ViewSet - takes 4 separate Views which are making     # 
# CRUD-functionality, and combines   them in 1 ViewSet  #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # 

from rest_framework import viewsets, routers
class ArticleViewSet(viewsets.ModelViewSet):
    serializer_class = ArticleSerializer
    queryset = Article.objects.all()

router = routers.DefaultRouter()
router.register('', ArticleViewSet, 'api')
urlpatterns = router.urls


