from django.urls import path
from . import views

urlpatterns = [
    path('trainers/', views.TrainersListView.as_view(), name='trainers_list_view'),
    path('trainer/<int:pk>/', views.TrainerDetailView.as_view(), name='trainer_detail_view'),
    path('trainer/add/', views.TrainerCreateView.as_view(), name='trainer_add_view'),
    path('trainer/del/<int:pk>/', views.TrainerDeleteView.as_view(), name='trainer_del_view'),
    path('trainer/update/<int:pk>/', views.TrainerUpdateView.as_view(), name='trainer_update_view'),
    path('students/', views.StudentsListView.as_view(), name='students_list_view'),
    path('student/<int:pk>/', views.StudentDetailView.as_view(), name='student_detail_view'),
    path('student/add/', views.StudentCreateView.as_view(), name='student_add_view'),
    path('student/del/<int:pk>/', views.StudentDeleteView.as_view(), name='student_del_view'),
    path('student/update/<int:pk>/', views.StudentUpdateView.as_view(), name='student_update_view'),
    path('consents/', views.ConsentsListView.as_view(), name='consents_list_view'),
    path('consent/<int:pk>/', views.ConsentDetailView.as_view(), name='consent_detail_view'),
    path('consent/add/', views.ConsentCreateView.as_view(), name='consent_add_view'),
    path('consent/del/<int:pk>/', views.ConsentDeleteView.as_view(), name='consent_del_view'),
    path('consent/update/<int:pk>/', views.ConsentUpdateView.as_view(), name='consent_update_view'),
]
