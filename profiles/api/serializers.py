from rest_framework import serializers


class HelloSerializers(serializers.Serializer):
    """Serializers a name field fpr testing our API"""
    name = serializers.CharField(max_length=10)
