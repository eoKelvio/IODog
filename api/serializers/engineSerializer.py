from rest_framework import serializers
from api.models.engine import Engine

class EngineSerializer(serializers.ModelSerializer):
    class Meta:
        model = Engine
        fields = '__all__'