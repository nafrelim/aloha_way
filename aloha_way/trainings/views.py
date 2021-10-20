from datetime import datetime


from django.shortcuts import render, redirect

# Create your views here.
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView

from trainings.forms import TrainingCreateForm, BookingCreateForm, AddPacketForStudentForm, TrainingAcceptanceForm,\
    StudentsTrainingUpdateForm
from trainings.models import Trainer, TrainingPacket, Student, TrainerTimetable, SEASONS, Booking, Training, \
    StudentTraining


class IndexView(View):

    def get(self, request):
        today = datetime.now().strftime('%Y-%m-%d')
        bookings_today = Booking.objects.filter(day=today).filter(cancellation=False).order_by('start_time')
        response = render(request, 'index.html', {'bookings': bookings_today})
        return response


class ContactView(View):
    pass
    # def get(self, request):
    #     try:
    #         contact = Page.objects.get(title='kontakt')
    #     except:
    #         contact = "#contact"
    #     description = contact.description.split('\r\n')
    #     title = contact.title.upper()
    #     return render(request, 'contact.html', {
    #         'title': title,
    #         'contact': description
    #     })


class AboutView(View):
    pass
    # def get(self, request):
    #     try:
    #         about = Page.objects.get(title='o aplikacji')
    #     except:
    #         about = "#about"
    #     slug= about.slug
    #     description = about.description.split('\r\n')
    #     title = about.title.upper()
    #     return render(request, slug + '.html', {
    #         'title': title,
    #         'contact': description
    #     })


class TrainersListView(ListView):
    model = Trainer
    template_name = 'trainers_list.html'


class DetailTrainerView(DetailView):
    model = Trainer
    template_name = 'trainer_detail.html'

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     trainer = Trainer.objects.get(pk=3)
    #     context['level'] = LEVELS[trainer.level][1]
    #     return context


class TrainerCreateView(CreateView):
    model = Trainer
    fields = '__all__'
    success_url = reverse_lazy("trainers_list_view")


class TrainerDeleteView(DeleteView):
    model = Trainer
    success_url = reverse_lazy("trainers_list_view")


class TrainerUpdateView(UpdateView):
    model = Trainer
    fields = ['phone', 'level', 'description']
    success_url = reverse_lazy("trainers_list_view")


class StudentsListView(ListView):
    model = Student
    template_name = 'students_list.html'


class DetailStudentView(DetailView):
    model = Student
    template_name = 'student_detail.html'


class StudentCreateView(CreateView):
    model = Student
    fields = ['first_name', 'last_name', 'email', 'phone', 'weight', 'height', 'consents', 'available_hours',
              'used_hours', 'description']
    success_url = reverse_lazy("students_list_view")


class StudentDeleteView(DeleteView):
    model = Student
    success_url = reverse_lazy("students_list_view")


class StudentUpdateView(UpdateView):
    model = Student
    fields = ['first_name', 'last_name', 'email', 'phone', 'weight', 'height', 'consents', 'available_hours',
              'used_hours', 'description']
    success_url = reverse_lazy("students_list_view")


class PacketsListView(ListView):
    model = TrainingPacket
    template_name = 'packets_list.html'


class DetailPacketView(DetailView):
    model = TrainingPacket
    template_name = 'packet_detail.html'


class PacketCreateView(CreateView):
    model = TrainingPacket
    fields = '__all__'
    success_url = reverse_lazy("packets_list_view")


class AddPacketForStudentView(View):
    def get(self, request, student_id):
        form = AddPacketForStudentForm
        student = Student.objects.get(pk=student_id)
        return render(request, 'add_packet_for_student_form.html', {
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


class PacketDeleteView(DeleteView):
    model = TrainingPacket
    success_url = reverse_lazy("packets_list_view")


class PacketUpdateView(UpdateView):
    model = TrainingPacket
    fields = '__all__'
    success_url = reverse_lazy("packets_list_view")


class TimetablesListView(View):

    def get(self, request, id):
        trainer = Trainer.objects.get(user_id=id)
        items = TrainerTimetable.objects.filter(trainer_id=id).filter(season=0).order_by('day')
        season = SEASONS[0][1]
        return render(request, 'timetables_list.html', {
            'items': items,
            'trainer': trainer,
            'season': season,
        })


class TimetableCreateView(CreateView):
    model = TrainerTimetable
    fields = '__all__'
    success_url = reverse_lazy("timetables_list_view")


class TimetableDeleteView(DeleteView):
    model = TrainerTimetable
    success_url = reverse_lazy("timetables_list_view")


class TimetableUpdateView(UpdateView):
    model = TrainerTimetable
    fields = '__all__'
    success_url = reverse_lazy("timetables_list_view")


class BookingsListView(ListView):
    queryset = Booking.objects.all().filter(cancellation=False).filter(was_training=False).order_by('day').\
        order_by('start_time')
    template_name = 'bookings_list.html'


class CanceledBookingsListView(ListView):
    queryset = Booking.objects.all().filter(cancellation=True).order_by('day').order_by('start_time')
    template_name = 'canceled_bookings_list.html'


class DetailBookingView(DetailView):
    model = Booking
    template_name = 'booking_detail.html'


# class BookingCreateView(CreateView):
#     model = Booking
#     fields = '__all__'
#     success_url = reverse_lazy("bookings_list_view")

class BookingCreateView(CreateView):
    model = Booking
    template_name = 'student_booking_form.html'
    fields = ['day', 'start_time', 'duration', 'trainer', 'students', 'description']
    success_url = reverse_lazy("bookings_list_view")


# class BookingCreateView(View):
#     def get(self, request):
#         form = BookingCreateForm
#         return render(request, 'booking_form.html', {
#             'form': form,
#         })
#
#     def post(self, request):
#         form = BookingCreateForm(request.POST)
#         if form.is_valid():
#             booking = form.save()
#             booking.save()
#         return redirect('/bookings/')


# class BookingCreateForStudentView(View):
#     form = BookingCreateForm
#     template_name = 'student_booking_form.html'
#     success_url = reverse_lazy("bookings_list_view")
#
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['student'] = Student.objects.get(pk=self.kwargs['student_id'])
#         return context
#


# class BookingCreateForStudentView(View):
#     def get(self, request, student_id):
#         student = Student.objects.get(pk=student_id)
#         form = BookingCreateForm
#         return render(request, 'student_booking_form.html', {
#             'form': form,
#             'student': student,
#         })
#
#     def post(self, request, student_id):
#         form = BookingCreateForm(request.POST)
#         student = Student.objects.get(pk=student_id)
#         if form.is_valid():
#             booking = form.save(commit=False)
#             booking.save()
#             booking.students.add(student)
#         return redirect('/students/')


class BookingDeleteView(DeleteView):
    model = Booking
    success_url = reverse_lazy("bookings_list_view")


class BookingCancelView(View):
    def get(self, request, booking_id):
        booking = Booking.objects.get(pk=booking_id)
        booking.cancellation = True
        booking.save()
        return redirect('/bookings/')


class BookingUpdateView(UpdateView):
    model = Booking
    fields = '__all__'
    success_url = reverse_lazy("bookings_list_view")


class TrainingsListView(ListView):
    model = Training
    template_name = 'trainings_list.html'


class DetailTrainingView(DetailView):
    model = Training
    template_name = 'training_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['students_training'] = StudentTraining.objects.filter(training_id=self.kwargs['pk'])
        return context


class TrainingCreateView(View):
    def get(self, request, booking_id):
        booking = Booking.objects.get(pk=booking_id)
        students = booking.students.all().order_by('last_name')
        form = TrainingCreateForm(initial={
            'start_time': booking.start_time,
            'trainer': booking.trainer,
            'duration': booking.duration,
            'students': students
        })
        return render(request, 'training_form.html', {
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
            return redirect(f'/trainings/')
        return redirect('/bookings/')


class TrainingStudentUpdateView(View):
    def get(self, request, pk):
        student_training = StudentTraining.objects.get(pk=pk)
        training = Training.objects.get(pk=student_training.training_id)
        form = StudentsTrainingUpdateForm
        return render(request, 'student_training_form.html', {
            'form': form,
            'student': student_training,
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


class TrainingDeleteView(DeleteView):
    model = Training
    success_url = reverse_lazy("training_list_view")


class TrainingUpdateView(UpdateView):
    model = Training
    fields = '__all__'
    success_url = reverse_lazy("training_list_view")


class TrainingAcceptanceView(View):
    def get(self, request, training_id):
        training = Training.objects.get(pk=training_id)
        students_training = StudentTraining.objects.filter(training_id=training_id)
        form = TrainingAcceptanceForm
        return render(request, 'training_acceptance.html', {
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
