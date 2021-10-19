from django import forms
from django.forms import ModelForm

from trainings.models import Training, Booking, TrainingPacket, Student


class AddPacketForStudentForm(forms.Form):
    packet = forms.ModelChoiceField(label='Wybierz pakiet', queryset=TrainingPacket.objects.filter(active=True))


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


class BookingCreateForm(ModelForm):
    class Meta:
        model = Booking
        exclude = ['cancellation']
        widgets = {
            'students': forms.SelectMultiple,
            'day': forms.SelectDateWidget,

        }

        labels = {'students': 'Kursanci'}


class TrainingCreateForm(ModelForm):
    class Meta:
        model = Training
        exclude = ['booking']
        widgets = {'students': forms.CheckboxSelectMultiple}
        labels = {'students': 'Kursanci'}


# class TrainingCreateForm(forms.Form):
#     booking = forms.CharField(label='Rezerwacja', disabled=True)
#     start_time = forms.DateTimeField(label='Godzina rozpoczęcia')
#     students =
#     for student in students:
#
#     duration = forms.IntegerField(label='Czas trwania(godz)', min_value=0, max_value=5)
#     trainer = forms.Select(label='Instruktor')
#     students = forms.ManyToManyField(Student, through="StudentTraining", verbose_name='Kursanci')
