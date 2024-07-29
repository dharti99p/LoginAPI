from rest_framework import serializers
from .models import LogIn


class LogInSerializer(serializers.ModelSerializer):
    class Meta:
        model = LogIn
        fields = '__all__'
