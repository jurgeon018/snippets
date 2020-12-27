from django.urls import path
from django.db import models
from django.contrib.auth.models import User
from rest_framework import routers, viewsets, permissions, serializers

# models.py
class Lead(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100, unique=True)
    message = models.CharField(max_length=500, blank=True)
    owner = models.ForeignKey(
        User, related_name="leads", on_delete=models.CASCADE, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

# serializers.py
# Lead Serializer - превращает модель Lead в сериалайзер, который отобразит ее в JSON-фомрате
class LeadSerializer(serializers.ModelSerializer):
  class Meta:
    model = Lead 
    fields = '__all__'

# api.py
# Lead Viewset. Viewset -  позволяет создать CRUD API, без необходимости описанияотдельных методов вручную 
class LeadViewSet(viewsets.ModelViewSet):
    queryset = Lead.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = LeadSerializer

    # permission_classes = [
    #     permissions.IsAuthenticated,
    # ]
    # serializer_class = LeadSerializer
    # def get_queryset(self):
    #     return self.request.user.leads.all()
    # def perform_create(self, serializer):
    #     serializer.save(owner=self.request.user)

# urls.py
router = routers.DefaultRouter()
router.register('api/leads', LeadViewSet, 'leads')
router.register('api/leadz', LeadViewSet, 'leads')
urlpatterns = router.urls
