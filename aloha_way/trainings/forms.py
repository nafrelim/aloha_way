from django import forms
from django.forms import ModelForm

from trainings.models import Training, Booking


class TrainingCreateForTrainerForm(ModelForm):
    class Meta:
        model = Training
        fields = '__all__'
        # exclude = ['trainer_id']

#
# class SelectBooking(forms.Form):
#     bookings = Booking.objects.all()
#     choices = ()
#     for booking in bookings:
#         tuple = (booking.id, booking.start_time)
#         choices += tuple
#     booking = forms.ChoiceField(choices=choices)


class SelectBooking(ModelForm):
    class Meta:
        model = Booking
        fields = ['id']


class TrainingCreateForm(ModelForm):
    class Meta:
        model = Training
        fields = '__all__'
        # exclude = ['trainer_id']


