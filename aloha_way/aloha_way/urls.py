"""aloha_way URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from trainings import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.IndexView.as_view(), name='index_view'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('trainers/', views.TrainersListView.as_view(), name='trainers_list_view'),
    path('trainer/<int:pk>/', views.DetailTrainerView.as_view(), name='detail_trainer_view'),
    path('trainer/add/', views.TrainerCreateView.as_view(), name='add_student_view'),
    path('trainer/del/<int:pk>/', views.TrainerDeleteView.as_view(), name='del_student_view'),
    path('trainer/update/<int:pk>/', views.TrainerUpdateView.as_view(), name='update_student_view'),
    path('add-trainer/', views.TrainerCreateView.as_view(), name='add_trainer_view'),
    path('students/', views.StudentsListView.as_view(), name='students_list_view'),
    path('student/<int:pk>/', views.DetailStudentView.as_view(), name='detail_student_view'),
    path('student/add/', views.StudentCreateView.as_view(), name='add_student_view'),
    path('student/del/<int:pk>/', views.StudentDeleteView.as_view(), name='del_student_view'),
    path('student/update/<int:pk>/', views.StudentUpdateView.as_view(), name='update_student_view'),
    path('packets/', views.PacketsListView.as_view(), name='packets_list_view'),
    path('packet/<int:pk>/', views.DetailPacketView.as_view(), name='detail_packet_view'),
    path('packet/add/', views.PacketCreateView.as_view(), name='add_packet_view'),
    path('packet/del/<int:pk>/', views.PacketDeleteView.as_view(), name='del_student_view'),
    path('packet/update/<int:pk>/', views.PacketUpdateView.as_view(), name='update_student_view'),
    path('timetables/<int:id>/', views.TimetablesListView.as_view(), name='timetables_list_view'),
    path('timetable/del/<int:pk>/', views.TimetableDeleteView.as_view(), name='timetable_del_view'),
    path('timetable/modify/<int:pk>/', views.TimetableUpdateView.as_view(), name='timetable_mod_view'),
    path('timetable/add/', views.TimetableCreateView.as_view(), name='add_timetable_view'),
    path('bookings/', views.BookingsListView.as_view(), name='bookings_list_view'),
    path('booking/<int:pk>/', views.DetailBookingView.as_view(), name='detail_booking_view'),
    path('booking/add/', views.BookingCreateView.as_view(), name='add_booking_view'),
    path('booking/add/<int:pk>/', views.BookingCreateForStudentView.as_view(), name='add_booking_student_view'),
    path('booking/del/<int:pk>/', views.BookingDeleteView.as_view(), name='del_booking_view'),
    path('booking/update/<int:pk>/', views.BookingUpdateView.as_view(), name='update_booking_view'),
    path('trainings/', views.TrainingsListView.as_view(), name='trainings_list_view'),
    path('training/<int:pk>/', views.DetailTrainingView.as_view(), name='detail_training_view'),
    path('training/add/', views.TrainingChoiceBookingView.as_view(), name='add_training_view'),
    path('training/add/<int:booking_id>/', views.TrainingCreateView.as_view(), name='add_training_trainer_view'),
    path('training/del/<int:pk>/', views.TrainingDeleteView.as_view(), name='del_training_view'),
    path('training/update/<int:pk>/', views.TrainingUpdateView.as_view(), name='update_training_view'),

    # path('accounts/', include('accounts.urls')),
]
