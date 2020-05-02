from rest_framework import routers
from .api import CatViewSet
from django.urls import path, include
from .views import CatsList

router = routers.DefaultRouter()
router.register('api/cats', CatViewSet, 'cats')

urlpatterns = [
    path('api/cats/pagination', CatsList),
    path('', include(router.urls))
]
