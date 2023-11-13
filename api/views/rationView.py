from rest_framework import viewsets
from api.models.ration import Ration
from api.serializers.rationSerializer import RationSerializer

class RationView(viewsets.ModelViewSet):
    queryset = Ration.objects.all()
    serializer_class = RationSerializer