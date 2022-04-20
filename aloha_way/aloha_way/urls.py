from django.contrib import admin
from django.urls import path, include

from trainings.views import IndexView, BookingViewSet, TrainingViewSet

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', IndexView.as_view(), name='index_view'),
    path('', include('trainings.urls')),
    path('', include('people.urls')),
    path('accounts/', include('accounts.urls')),
    path('api-auth/', include('rest_framework.urls'), name='rest_framework'),
]
