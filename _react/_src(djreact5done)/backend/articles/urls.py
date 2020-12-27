from django.urls import path
from rest_framework.generics import ListAPIView, RetrieveAPIView, CreateAPIView, DestroyAPIView, UpdateAPIView
from django.db import models
from django.contrib import admin
from rest_framework import serializers, routers, viewsets, permissions

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
    permission_classes = (permissions.AllowAny, )

class ArticleDetailView(RetrieveAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    permission_classes = (permissions.AllowAny, )

class ArticleCreateView(CreateAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    permission_classes = (permissions.IsAuthenticated, )

class ArticleUpdateView(UpdateAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    permission_classes = (permissions.IsAuthenticated, )

class ArticleDeleteView(DestroyAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    permission_classes = (permissions.IsAuthenticated, )





urlpatterns = [
    path('', ArticleListView.as_view()),
    path('<pk>', ArticleDetailView.as_view()),
    # path('create/', ArticleCreateView.as_view()),
    # path('<pk>/update/', ArticleUpdateView.as_view()),
    # path('<pk>/delete/', ArticleDeleteView.as_view())
]


# class ArticleViewSet(viewsets.ModelViewSet):
#     serializer_class = ArticleSerializer
#     queryset = Article.objects.all()
#     permission_classes = [permissions.AllowAny]

# router = routers.DefaultRouter()
# router.register('', ArticleViewSet, 'articles')
# urlpatterns = router.urls
