from rest_framework import serializers
from api.models.proximity import Proximity

class ProximitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Proximity
        fields = ['is_closed', 'created_at']