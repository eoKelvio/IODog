from rest_framework import viewsets
from api.models.proximity import Proximity
from api.serializers.proximitySerializer import ProximitySerializer

class ProximityView(viewsets.ModelViewSet):
    queryset = Proximity.objects.all()
    serializer_class = ProximitySerializer