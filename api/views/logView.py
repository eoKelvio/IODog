from rest_framework import viewsets
from api.models.log import Log
from api.serializers.logSerializer import LogSerializer

class LogView(viewsets.ModelViewSet):
    queryset = Log.objects.all()
    serializer_class = LogSerializer