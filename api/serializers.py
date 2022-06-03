"""Serializers module."""
from rest_framework import serializers

from api.models import Logs


class LogsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Logs
        fields = "__all__"


class LogsFileUploadSerializer(serializers.Serializer):
    file = serializers.FileField()
