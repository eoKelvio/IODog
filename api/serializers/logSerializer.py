from rest_framework import serializers
from api.models.log import Log

class LogSerializer(serializers.Serializer):
    class Meta:
        model = Log
        fields = '__all__'
