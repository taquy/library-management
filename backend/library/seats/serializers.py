
from seats.models import Seat
from rest_framework import serializers

class SeatSerializer(serializers.ModelSerializer):
  
    class Meta:
        model = Seat
        fields = ['id', 'name', 'age']
        read_only_fields = ['id']

    def create(self, data):
        query = Seat(
            name = data['name'],
            age = data['age'],
        )
        query.save()
        return query