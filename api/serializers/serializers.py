from rest_framework import serializers
from api.models.models import CategoryModels

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = CategoryModels
        fields = ['id', 'name']