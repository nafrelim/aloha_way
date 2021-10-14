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
    path('add-trainer/', views.TrainerCreateView.as_view(), name='add_trainer_view'),
    path('students/', views.StudentsListView.as_view(), name='students_list_view'),
    path('student/<int:pk>/', views.DetailStudentView.as_view(), name='detail_trainer_view'),
    path('packets/', views.PacketsListView.as_view(), name='packets_list_view'),
    path('packet/<int:pk>/', views.DetailPacketView.as_view(), name='detail_trainer_view'),
    path('add-packet/', views.PacketCreateView.as_view(), name='add_packet_view'),
    path('timetables/<int:id>/', views.TimetablesListView.as_view(), name='timetables_list_view'),
    # path('accounts/', include('accounts.urls')),
]
