
from django.urls import path, include
from rest_framework import routers
from licenses.views import ClientViewSet, LicenseViewSet, LogEmailViewSet
from .api.views import EmailNotificationAPIView 
router=routers.DefaultRouter()
router.register(r'clients', ClientViewSet)
router.register(r'licenses', LicenseViewSet)
router.register(r'logemail', LogEmailViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('send-email-notifications/', EmailNotificationAPIView.as_view(), name='send-email-notifications'),
]