from rest_framework import serializers
from datetime import date
from .models import Client

class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = "all"

    def validate_birth_date(self, value):
        if value > date.today():
            raise serializers.ValidationError("Дата рождения не может быть в будущем")
        
        return value