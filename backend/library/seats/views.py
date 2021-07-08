
from seats.serializers import SeatSerializer
from seats.models import Seat
from rest_framework.decorators import action
from rest_framework import status, viewsets
from rest_framework.response import Response

class SeatsViewSet(viewsets.ViewSet):
  
    def list(self, request):
      
      seats = Seat.objects.all().order_by('age')
      serializer = SeatSerializer(seats)
      return Response(serializer.data)

    def create(self, request):
      pass

    def retrieve(self, request, pk=None):
      return Response({
        'status': 'ok'
      })

    def update(self, request, pk=None):
      pass

    def partial_update(self, request, pk=None):
      pass

    def destroy(self, request, pk=None):
      pass