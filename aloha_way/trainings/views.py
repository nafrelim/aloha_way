from datetime import datetime

from django.shortcuts import render

# Create your views here.
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView

from trainings.models import Trainer, TrainingPacket, Student, TrainerTimetable, SEASONS


class IndexView(View):

    def get(self, request):
        response = render(request, 'base.html')
        return response


class DashboardView(View):
    pass
    # def get(self, request):
    #     plan = Plan.objects.order_by('-created').first()
    #     recipe_plans = RecipePlan.objects.filter(plan_id=plan.id).all()
    #     return render(request, "dashboard.html", dict(
    #         recipes_count=Recipe.objects.all().count(),
    #         plans_count=Plan.objects.all().count(),
    #         day_names=DayName.objects.all().order_by('order'),
    #         last_added_plan=plan,
    #         recipe_plans=recipe_plans
    #     ))


class MainPage(View):
    pass
    # def get(self, request):
    #     recipes = Recipe.objects.all()
    #     array = []
    #     for recipe in recipes:
    #         array.append(recipe.id)
    #     shuffle(array)
    #     try:
    #         about = '/' + Page.objects.get(title='o aplikacji').slug
    #         contact = '/' + Page.objects.get(title='kontakt').slug
    #     except:
    #         about = "#about"
    #         contact = "#contact"
    #     try:
    #         recipe1 = Recipe.objects.get(id=array[0])
    #         recipe2 = Recipe.objects.get(id=array[1])
    #         recipe3 = Recipe.objects.get(id=array[2])
    #         resp = {
    #             "recipe1": recipe1,
    #             "recipe2": recipe2,
    #             "recipe3": recipe3,
    #             "about": about,
    #             "contact": contact,
    #         }
    #     except IndexError:
    #         empty = {
    #             "name": "Nie ma przepisów!",
    #             "description": "Wprowadź minimum 3 przepisy do bazy danych."
    #         }
    #         resp = {
    #             "recipe1": empty,
    #             "recipe2": empty,
    #             "recipe3": empty,
    #             "about": about,
    #             "contact": contact,
    #         }
    #     return render(request, 'index.html', resp)


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


class TrainerCreateView(CreateView):
    model = Trainer
    fields = '__all__'
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

