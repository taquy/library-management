from seats.serializers import SeatSerializer
from django.shortcuts import render

# Create your views here.

from seats.models import Seat
from rest_framework.decorators import action
from rest_framework import status, viewsets
from rest_framework.response import Response

class SeatsViewSet(viewsets.ViewSet):
  
    def list(self, request):
      seats = Seat.objects.all().order_by('age')
      serializer = SeatSerializer(seats, many=True)
      return Response(serializer.data)

    def create(self, request):
      serializer = SeatSerializer()
      result = serializer.create(request.data)
      serializer = SeatSerializer(result)
      return Response(serializer.data)

    def retrieve(self, request, pk=None):
      result = Seat.objects.get(pk=pk)
      serializer = SeatSerializer(result)
      return Response(serializer.data)

    def update(self, request, pk=None):
      result = Seat.objects.filter(pk=pk).update(
        name=request.data['name'],
        age=request.data['age'],
      )
      result = Seat.objects.get(pk=pk)
      serializer = SeatSerializer(result)
      return Response(serializer.data)

    def destroy(self, request, pk=None):
      result = Seat.objects.get(pk=pk)
      result.delete()
      seats = Seat.objects.all().order_by('age')
      serializer = SeatSerializer(seats, many=True)
      return Response(serializer.data)