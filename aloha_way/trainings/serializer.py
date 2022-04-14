from rest_framework import serializers

from .models import Training, Booking


class BookingSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Booking
        fields = ['id', 'start_time', 'duration']


class TrainingSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Training
        fields = ['id', 'booking', 'day', 'start_time', 'duration', 'acceptance']
