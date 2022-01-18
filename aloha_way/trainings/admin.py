from django.contrib import admin

# Register your models here.
from .models import *

admin.site.register(TrainingPacket)
admin.site.register(Booking)
admin.site.register(Training)
admin.site.register(StudentTraining)
