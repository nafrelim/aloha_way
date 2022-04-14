from django.contrib import admin

from .models import *


@admin.register(TrainingPacket)
class TrainingPacketAdmin(admin.ModelAdmin):
    list_display = ('name', 'number_of_hours', 'price', 'is_active')


@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_filter = ('trainer__user__last_name', 'duration', 'day')
    list_display = ('__str__', 'trainer')
    search_fields = ['trainer__user__last_name']


@admin.register(Training)
class TrainingAdmin(admin.ModelAdmin):
    list_filter = ('booking', 'trainer__user__last_name', 'day', 'acceptance')
    list_display = ('__str__', 'booking', 'trainer', 'acceptance')
    search_fields = ['trainer__user__last_name']


@admin.register(StudentTraining)
class StudentTrainingAdmin(admin.ModelAdmin):
    pass
    # list_display = ('__str__')




