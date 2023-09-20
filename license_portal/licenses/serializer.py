from rest_framework import serializers
from .models import Client, License


class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = '__all__'
