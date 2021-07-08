
from rest_framework import serializers

class SeatSerializer(serializers.Serializer):
  name = serializers.CharField(max_length=30)
  age = serializers.CharField(max_length=30)