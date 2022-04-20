from rest_framework import serializers

from django.contrib.auth.models import User

from people.models import Trainer, Student
from .models import Training, Booking


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']


class BookingSerializer(serializers.HyperlinkedModelSerializer):
    # trainer = serializers.SlugRelatedField(slug_field='user', queryset=Trainer.objects.all())
    # doesnt't work. exception "Object of type User is not JSON serializable

    students = serializers.SlugRelatedField(many=True, slug_field='last_name', queryset=Student.objects.all())

    class Meta:
        model = Booking
        fields = ['id', 'day', 'start_time', 'duration', 'students']


class TrainingSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Training
        fields = ['id', 'booking', 'day', 'start_time', 'duration', 'acceptance']
