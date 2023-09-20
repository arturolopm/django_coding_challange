
from django.urls import path, include
from rest_framework import routers
from licenses.views import ClientViewSet
router=routers.DefaultRouter()
router.register(r'clients', ClientViewSet)

urlpatterns = [
    path('', include(router.urls))
]