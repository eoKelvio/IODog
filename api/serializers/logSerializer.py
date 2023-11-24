from rest_framework import serializers
from api.models.log import Log

class LogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Log
        fields = '__all__'
