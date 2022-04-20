from django.urls import path, include
from . import views

from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'bookings', views.BookingViewSet)
router.register(r'trainings', views.TrainingViewSet)
router.register(r'users', views.UserViewSet)


urlpatterns = [
    path('packets/', views.PacketsListView.as_view(), name='packets_list_view'),
    path('packet/<int:pk>/', views.PacketDetailView.as_view(), name='packet_detail_view'),
    path('packet/add/', views.PacketCreateView.as_view(), name='packet_add_view'),
    path('packet/add/<int:student_id>', views.AddPacketForStudentView.as_view(), name='packet_add_for_student_view'),
    path('packet/del/<int:pk>/', views.PacketDeleteView.as_view(), name='packet_del_view'),
    path('packet/update/<int:pk>/', views.PacketUpdateView.as_view(), name='packet_update_view'),
    path('bookings/', views.BookingsListView.as_view(), name='bookings_list_view'),
    path('bookings_cancelled/', views.CancelledBookingsListView.as_view(), name='cancelled_bookings_list_view'),
    path('booking/<int:pk>/', views.BookingDetailView.as_view(), name='booking_detail_view'),
    path('booking/add/', views.BookingCreateView.as_view(), name='booking_add_view'),
    path('booking/del/<int:pk>/', views.BookingDeleteView.as_view(), name='booking_del_view'),
    path('booking/update/<int:pk>/', views.BookingUpdateView.as_view(), name='booking_update_view'),
    path('booking/cancel/<int:booking_id>/', views.BookingCancelView.as_view(), name='booking_cancel_view'),
    path('trainings/', views.TrainingsListView.as_view(), name='trainings_list_view'),
    path('trainings_accepted/', views.AcceptedTrainingsListView.as_view(), name='accepted_trainings_list_view'),
    path('training/<int:pk>/', views.TrainingDetailView.as_view(), name='training_detail_view'),
    path('training/add/<int:booking_id>/', views.TrainingCreateView.as_view(), name='training_add_view'),
    path('training/student/<int:pk>', views.TrainingStudentUpdateView.as_view(), name='training_student_update_view'),
    path('training/del/<int:pk>/', views.TrainingDeleteView.as_view(), name='training_del_view'),
    path('training/update/<int:pk>/', views.TrainingUpdateView.as_view(), name='training_update_view'),
    path('training/accept/<int:training_id>/', views.TrainingAcceptView.as_view(), name='training_accept_view'),
    path('api/', include(router.urls)),
]
