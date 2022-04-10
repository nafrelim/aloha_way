from django.contrib import admin

from .models import *


@admin.register(Consent)
class ConsentAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')


@admin.register(Trainer)
class TrainerAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'phone')


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'phone')


admin.site.register(TrainerTimetable)
admin.site.register(StudentConsent)
