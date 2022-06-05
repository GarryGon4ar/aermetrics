"""Serializers module."""
from rest_framework import serializers


class LogsFileUploadSerializer(serializers.Serializer):
    file = serializers.FileField()
