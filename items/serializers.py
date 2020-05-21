from rest_framework import serializers
from .models import Items


class ItemsSerializer(serializers.ModelSerializer):
    """ serializer for Items"""
    class Meta:
        model = Items
        fields = ('id', 'name', 'description', 'price', 'image')
