from rest_framework import routers
from .api import ProyectViewSet

router= routers.DefaultRouter()
router.register('api/Proyecto', ProyectViewSet, 'Proyecto')

urlpatterns= router.urls 