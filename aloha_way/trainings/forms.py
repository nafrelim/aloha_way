from django import forms
from django.forms import ModelForm

from trainings.models import Training, Booking, TrainingPacket, Student, StudentTraining


class AddPacketForStudentForm(forms.Form):
    packet = forms.ModelChoiceField(label='Wybierz pakiet', queryset=TrainingPacket.objects.filter(is_active=True))


class StudentsTrainingUpdateForm(ModelForm):
    class Meta:
        model = StudentTraining
        fields = ['duration']


class TrainingCreateForm(ModelForm):
    class Meta:
        model = Training
        exclude = ['booking', 'acceptance']
        # widgets = {'students': forms.CheckboxSelectMultiple}
        labels = {'students': 'Kursanci'}


class TrainingAcceptanceForm(forms.Form):
    booking = forms.BooleanField(label='Akceptacja?', initial=True)
