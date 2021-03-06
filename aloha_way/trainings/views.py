from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.shortcuts import render, redirect
from datetime import datetime
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView
from rest_framework.viewsets import ModelViewSet
from django.contrib.auth.models import User

from .models import TrainingPacket, Booking, Training, StudentTraining
from people.models import Trainer, Student
from .serializer import BookingSerializer, TrainingSerializer, UserSerializer

from .forms import TrainingCreateForm, AddPacketForStudentForm, TrainingAcceptanceForm, StudentsTrainingUpdateForm


class IndexView(View):
    """
    Main view
    """
    def get(self, request):
        today = datetime.now().strftime('%Y-%m-%d')
        bookings_today = Booking.objects.filter(day=today).filter(cancellation=False).filter(was_training=False).\
            order_by('start_time')
        return render(request, 'trainings/index.html', {'bookings': bookings_today})


class PacketsListView(LoginRequiredMixin, ListView):
    """
    List of available training packages
    """
    model = TrainingPacket
    template_name = 'trainings/packets_list.html'


class PacketDetailView(LoginRequiredMixin, DetailView):
    model = TrainingPacket
    template_name = 'trainings/packet_detail.html'


class PacketCreateView(LoginRequiredMixin, CreateView):
    model = TrainingPacket
    fields = '__all__'
    success_url = reverse_lazy('packets_list_view')


class AddPacketForStudentView(LoginRequiredMixin, View):

    def get(self, request, student_id):
        form = AddPacketForStudentForm
        student = Student.objects.get(pk=student_id)
        return render(request, 'trainings/add_packet_for_student_form.html', {
            'form': form,
            'student': student
        })

    def post(self, request, student_id):
        student = Student.objects.get(pk=student_id)
        form = AddPacketForStudentForm(request.POST)
        if form.is_valid():
            packet = form.cleaned_data['packet']
            student.available_hours += packet.number_of_hours
            student.save()
        return redirect(f'/student/{student_id}')


class PacketDeleteView(LoginRequiredMixin, DeleteView):
    model = TrainingPacket
    success_url = reverse_lazy('packets_list_view')


class PacketUpdateView(LoginRequiredMixin, UpdateView):
    model = TrainingPacket
    fields = '__all__'
    success_url = reverse_lazy('packets_list_view')


# class TimetablesListView(View):
#
#     def get(self, request, id):
#         trainer = Trainer.objects.get(user_id=id)
#         items = TrainerTimetable.objects.filter(trainer_id=id).filter(season=0).order_by('day')
#         season = SEASONS[0][1]
#         return render(request, 'timetables_list.html', {
#             'items': items,
#             'trainer': trainer,
#             'season': season,
#         })
#
#
# class TimetableCreateView(CreateView):
#     model = TrainerTimetable
#     fields = '__all__'
#     success_url = reverse_lazy('timetables_list_view')
#
#
# class TimetableDeleteView(DeleteView):
#     model = TrainerTimetable
#     success_url = reverse_lazy('timetables_list_view')
#
#
# class TimetableUpdateView(UpdateView):
#     model = TrainerTimetable
#     fields = '__all__'
#     success_url = reverse_lazy('timetables_list_view')


class BookingsListView(LoginRequiredMixin, ListView):
    queryset = Booking.objects.filter(cancellation=False).filter(was_training=False).order_by('day').\
        order_by('start_time')
    template_name = 'trainings/bookings_list.html'


class CancelledBookingsListView(LoginRequiredMixin, ListView):
    queryset = Booking.objects.filter(cancellation=True).order_by('day').order_by('start_time')
    template_name = 'trainings/canceled_bookings_list.html'


class BookingDetailView(LoginRequiredMixin, DetailView):
    model = Booking
    template_name = 'trainings/booking_detail.html'


class BookingCreateView(LoginRequiredMixin, CreateView):
    model = Booking
    # template_name = 'booking_form.html'
    fields = ['day', 'start_time', 'duration', 'trainer', 'students', 'description']
    success_url = reverse_lazy('bookings_list_view')


class BookingDeleteView(LoginRequiredMixin, DeleteView):
    model = Booking
    success_url = reverse_lazy('bookings_list_view')


class BookingCancelView(LoginRequiredMixin, View):
    def get(self, request, booking_id):
        booking = Booking.objects.get(pk=booking_id)
        booking.cancellation = True
        booking.save()
        return redirect('bookings_list_view')


class BookingUpdateView(LoginRequiredMixin, UpdateView):
    model = Booking
    fields = '__all__'
    success_url = reverse_lazy('bookings_list_view')


class TrainingsListView(LoginRequiredMixin, ListView):
    queryset = Training.objects.filter(acceptance=False).order_by('day').order_by('start_time')
    template_name = 'trainings/trainings_list.html'


class AcceptedTrainingsListView(LoginRequiredMixin, ListView):
    queryset = Training.objects.filter(acceptance=True).order_by('day').order_by('start_time')
    template_name = 'trainings/accepted_trainings_list.html'


class TrainingDetailView(LoginRequiredMixin, DetailView):
    model = Training
    template_name = 'trainings/training_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['students_training'] = StudentTraining.objects.filter(training_id=self.kwargs['pk'])
        return context


class TrainingCreateView(LoginRequiredMixin, View):
    def get(self, request, booking_id):
        booking = Booking.objects.get(pk=booking_id)
        students = booking.students.all().order_by('last_name')
        form = TrainingCreateForm(initial={
            'start_time': booking.start_time,
            'trainer': booking.trainer,
            'duration': booking.duration,
            'students': students
        })
        return render(request, 'trainings/training_form.html', {
            'form': form,
            'booking': booking,
            'students': booking.students.all()
        })

    def post(self, request, booking_id):
        form = TrainingCreateForm(request.POST)
        if form.is_valid():
            training = form.save(commit=False)
            training.booking_id = booking_id
            booking = Booking.objects.get(pk=booking_id)
            booking.was_training = True
            booking.save()
            training.save()
            form.save_m2m()
            student_trainings = StudentTraining.objects.filter(training_id=training.id)
            for item in student_trainings:
                item.duration = training.duration
                item.save()
            return redirect('trainings_list_view')
        return redirect('bookings_list_view')


class TrainingStudentUpdateView(LoginRequiredMixin, View):
    def get(self, request, pk):
        training_student = StudentTraining.objects.get(pk=pk)
        training = Training.objects.get(pk=training_student.training_id)
        form = StudentsTrainingUpdateForm
        return render(request, 'student_training_form.html', {
            'form': form,
            'student': training_student,
            'training': training
        })

    def post(self, request, pk):
        form = StudentsTrainingUpdateForm(request.POST)
        if form.is_valid():
            duration = form.cleaned_data
            student_training = StudentTraining.objects.get(pk=pk)
            student_training.duration = duration['duration']
            student_training.save()
            return redirect(f'/training/{student_training.training_id}')


class TrainingDeleteView(LoginRequiredMixin, DeleteView):
    model = Training
    success_url = reverse_lazy('trainings_list_view')


class TrainingUpdateView(LoginRequiredMixin, UpdateView):
    model = Training
    fields = '__all__'
    success_url = reverse_lazy('trainings_list_view')


class TrainingAcceptView(LoginRequiredMixin, View):
    def get(self, request, training_id):
        training = Training.objects.get(pk=training_id)
        students_training = StudentTraining.objects.filter(training_id=training_id)
        form = TrainingAcceptanceForm
        return render(request, 'trainings/training_acceptance.html', {
            'form': form,
            'training': training,
            'students_training': students_training
        })

    def post(self, request, training_id):
        form = TrainingAcceptanceForm(request.POST)
        if form.is_valid():
            acceptance = form.cleaned_data
            if acceptance:
                training = Training.objects.get(pk=training_id)
                training.acceptance = True
                training.save()
                trainer = Trainer.objects.get(pk=training.trainer_id)
                trainer.hours_completed += training.duration
                trainer.save()
                student_trainings = StudentTraining.objects.filter(training_id=training.id)
                for item in student_trainings:
                    item.duration = training.duration
                    item.student.available_hours -= training.duration
                    item.student.used_hours += training.duration
                    item.save()
                    item.student.save()
        return redirect('/trainings/')


class BookingViewSet(ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer


class TrainingViewSet(ModelViewSet):
    queryset = Training.objects.all()
    serializer_class = TrainingSerializer


class UserViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
