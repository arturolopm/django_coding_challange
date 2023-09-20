from rest_framework import serializers
from .models import Client, License, LogEmail


class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = '__all__'
class LicenseSerializer(serializers.ModelSerializer):
    class Meta:
        model = License
        fields = '__all__'
class LogEmailSerializer(serializers.ModelSerializer):
    class Meta:
        model = LogEmail
        fields = '__all__'
