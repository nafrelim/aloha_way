from django import forms
from django.forms import ModelForm

from trainings.models import Training, Booking, TrainingPacket, Student, StudentTraining


class AddPacketForStudentForm(forms.Form):
    packet = forms.ModelChoiceField(label='Wybierz pakiet', queryset=TrainingPacket.objects.filter(active=True))


# class TrainingCreateForTrainerForm(ModelForm):
#     class Meta:
#         model = Training
#         fields = '__all__'
#         # exclude = ['trainer_id']


class BookingCreateForm(ModelForm):
    class Meta:
        model = Booking
        exclude = ['cancellation', 'was_training', ]
        widgets = {
            'students': forms.SelectMultiple,
            'day': forms.SelectDateWidget,

        }
        labels = {'students': 'Kursanci'}


class TrainingCreateForm(ModelForm):
    class Meta:
        model = Training
        exclude = ['booking', 'acceptance']
        # widgets = {'students': forms.CheckboxSelectMultiple}
        labels = {'students': 'Kursanci'}


class StudentsTrainingUpdateForm(ModelForm):
    class Meta:
        model = StudentTraining
        fields = ['duration']


class TrainingAcceptanceForm(forms.Form):
    booking = forms.BooleanField(label='Akceptacja?', initial=True)
