from rest_framework import viewsets
from api.models.engine import Engine
from api.serializers.engineSerializer import EngineSerializer

class EngineView(viewsets.ModelViewSet):
    queryset = Engine.objects.all()
    serializer_class = EngineSerializer