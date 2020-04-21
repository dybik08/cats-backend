from cats.models import Cat
from rest_framework import viewsets, permissions
from .serializers import CatSerializer


class CatViewSet(viewsets.ModelViewSet):
    queryset = Cat.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = CatSerializer
