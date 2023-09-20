from rest_framework import viewsets
from .models import Client, License, LogEmail
from .serializer import ClientSerializer, LicenseSerializer, LogEmailSerializer

class ClientViewSet(viewsets.ModelViewSet):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer
class LicenseViewSet(viewsets.ModelViewSet):
    queryset = License.objects.all()
    serializer_class = LicenseSerializer
class LogEmailViewSet(viewsets.ModelViewSet):
    queryset = LogEmail.objects.all()
    serializer_class = LogEmailSerializer

