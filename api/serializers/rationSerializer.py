from rest_framework import serializers
from api.models.ration import Ration

class ProximitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Ration
        fields = ['level', 'created_at']