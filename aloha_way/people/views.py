from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView
from people.models import Trainer, Student, Consent


class TrainersListView(LoginRequiredMixin, ListView):
    model = Trainer
    template_name = 'people/trainers_list.html'


class TrainerDetailView(LoginRequiredMixin, DetailView):
    model = Trainer
    template_name = 'people/trainer_detail.html'


class TrainerCreateView(LoginRequiredMixin, CreateView):
    model = Trainer
    fields = ['user', 'phone', 'level', 'description']
    success_url = reverse_lazy('trainers_list_view')


class TrainerDeleteView(LoginRequiredMixin, DeleteView):
    model = Trainer
    success_url = reverse_lazy('trainers_list_view')


class TrainerUpdateView(LoginRequiredMixin, UpdateView):
    model = Trainer
    fields = ['phone', 'level', 'description']
    success_url = reverse_lazy('trainers_list_view')


class StudentsListView(PermissionRequiredMixin, ListView):
    permission_required = ['people.view_student']
    model = Student
    template_name = 'people/students_list.html'


class StudentDetailView(LoginRequiredMixin, DetailView):
    model = Student
    template_name = 'people/student_detail.html'


class StudentCreateView(LoginRequiredMixin, CreateView):
    model = Student
    fields = ['first_name', 'last_name', 'email', 'phone', 'weight', 'height', 'consents', 'available_hours',
              'description']
    success_url = reverse_lazy('students_list_view')


class StudentDeleteView(LoginRequiredMixin, DeleteView):
    model = Student
    success_url = reverse_lazy('students_list_view')


class StudentUpdateView(LoginRequiredMixin, UpdateView):
    model = Student
    fields = ['first_name', 'last_name', 'email', 'phone', 'weight', 'height', 'consents', 'available_hours',
              'used_hours', 'description']
    success_url = reverse_lazy('students_list_view')


class ConsentsListView(PermissionRequiredMixin, ListView):
    permission_required = ['people.view_consent']
    model = Consent
    template_name = 'people/consents_list.html'


class ConsentDetailView(LoginRequiredMixin, DetailView):
    model = Consent
    template_name = 'people/consent_detail.html'


class ConsentCreateView(LoginRequiredMixin, CreateView):
    model = Consent
    fields = ['name', 'description']
    success_url = reverse_lazy('consent_list_view')


class ConsentDeleteView(LoginRequiredMixin, DeleteView):
    model = Consent
    success_url = reverse_lazy('consents_list_view')


class ConsentUpdateView(LoginRequiredMixin, UpdateView):
    model = Consent
    fields = ['name', 'description']
    success_url = reverse_lazy('consents_list_view')