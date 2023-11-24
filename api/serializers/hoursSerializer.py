from rest_framework import serializers
from api.models.hours import Hours

class HoursSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hours
        fields = '__all__'