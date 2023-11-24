from rest_framework import viewsets
from rest_framework.response import Response  # Adicione esta importação
from api.models.feedTimes import FeedTimes
from api.serializers.feedTimesSerializer import FeedTimesSerializer
from api.models.hours import Hours
from datetime import datetime

class FeedTimesView(viewsets.ModelViewSet):
    queryset = FeedTimes.objects.all()
    serializer_class = FeedTimesSerializer

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        # Atualizar o campo feed_time com todos os horários do modelo Hours
        all_hours = Hours.objects.all()
        instance.feed_time.set(all_hours)
        instance.current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        serializer = self.get_serializer(instance)
        return Response(serializer.data)
    
       

        instance.save() 

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        # Atualizar o campo feed_time com todos os horários do modelo Hours
        all_hours = Hours.objects.all()
        instance.feed_time.set(all_hours)
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data)
