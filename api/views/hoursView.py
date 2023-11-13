from rest_framework import viewsets
from api.models.hours import Hours
from api.serializers.hoursSerializer import HoursSerializer

class HoursView(viewsets.ModelViewSet):
    queryset = Hours.objects.all()
    serializer_class = HoursSerializer