from rest_framework import routers
from .api import CatViewSet

router = routers.DefaultRouter()
router.register('api/cats', CatViewSet, 'cats')

urlpatterns = router.urls
