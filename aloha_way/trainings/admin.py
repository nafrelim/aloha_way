from django.contrib import admin

from .models import *


@admin.register(TrainingPacket)
class TrainingPacketAdmin(admin.ModelAdmin):
    list_display = ('name', 'number_of_hours', 'price', 'is_active')


@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_filter = ('trainer', 'duration', 'day') # nue filtruje po trainer
    list_display = ('__str__', 'trainer')
    # search_fields = ['trainer'] # wywala sie


@admin.register(Training)
class TraingAdmin(admin.ModelAdmin):
    pass
    # list_display = ('__str__')


@admin.register(StudentTraining)
class StudentTraingAdmin(admin.ModelAdmin):
    pass
    # list_display = ('__str__')




