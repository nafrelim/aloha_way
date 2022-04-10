from django.db import models
from django.contrib.auth.models import User

from people.models import Trainer, Student


class TrainingPacket(models.Model):
    """
    Training packages that can be purchased by the student
    """

    name = models.CharField(max_length=50, verbose_name='Nazwa')
    number_of_hours = models.PositiveSmallIntegerField(verbose_name='Liczba godzin')
    price = models.PositiveSmallIntegerField(verbose_name='Cena')
    is_active = models.BooleanField(default=False, verbose_name='Aktywny')
    description = models.TextField(null=True, blank=True, verbose_name='Dodatkowe informacje')

    class Meta:
        ordering = ['is_active', 'number_of_hours']
        verbose_name_plural = 'Pakiety treningowe'

    def __str__(self):
        return f'{self.name}'


class Booking(models.Model):
    """
    Training booking: one instructor, one or more students
    """

    day = models.DateField(verbose_name='Dzień szkolenia')
    start_time = models.TimeField(verbose_name='Godzina rozpoczęcia')
    duration = models.PositiveSmallIntegerField(default=1, verbose_name='Czas trwania(godz)')
    trainer = models.ForeignKey(Trainer, on_delete=models.CASCADE, verbose_name='Instruktor')
    students = models.ManyToManyField(Student, verbose_name='Kursanci')
    cancellation = models.BooleanField(default=False, blank=True, verbose_name='Anulowanie?')
    was_training = models.BooleanField(default=False, blank=True, null=True, verbose_name='Szkolenie odbyte?')
    description = models.TextField(null=True, blank=True, verbose_name='Dodatkowe informacje')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['day', 'start_time']
        verbose_name_plural = 'Rezerwacje'

    def __str__(self):
        d = self.day.strftime('%Y-%m-%d')
        h = self.start_time.strftime('%H:%M')
        return f'start: {d} {h}, {self.duration} godz., {self.trainer.user.last_name} {self.trainer.user.first_name}'


class Training(models.Model):
    booking = models.OneToOneField(Booking, on_delete=models.CASCADE, verbose_name='Rezerwacja')
    day = models.DateField(auto_now_add=True, verbose_name='Dzień szkolenia')
    start_time = models.TimeField(verbose_name='Godzina rozpoczęcia')
    duration = models.PositiveSmallIntegerField(default=0, verbose_name='Czas trwania(godz)')
    trainer = models.ForeignKey(Trainer, on_delete=models.CASCADE, verbose_name='Instruktor')
    students = models.ManyToManyField(Student, through="StudentTraining", verbose_name='Kursanci')
    acceptance = models.BooleanField(default=False, verbose_name='Akceptacja')
    description = models.TextField(null=True, blank=True, verbose_name='Dodatkowe informacje')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['day', 'start_time']
        verbose_name_plural = 'Szkolenia'

    def __str__(self):
        d = self.day.strftime('%Y-%m-%d')
        h = self.start_time.strftime('%H:%M')
        return f'start: {d}, {h}, {self.duration} godz., {self.trainer.user.last_name} {self.trainer.user.first_name}'


class StudentTraining(models.Model):

    """
    Intermediate model between Student and Training
    Stores the number of hours spent by a specific student on a specific training
    The time spent on training together may be different for each student (e.g. an injury during training)
    The training may take a different length of time than planned in the booking (e.g. due to weather conditions)
    """

    student = models.ForeignKey(Student, on_delete=models.CASCADE, verbose_name='Instruktor')
    training = models.ForeignKey(Training, on_delete=models.CASCADE, verbose_name='Trening')
    duration = models.PositiveSmallIntegerField(default=0, verbose_name='Czas trwania')
    description = models.TextField(null=True, blank=True, verbose_name='Dodatkowe informacje')

    class Meta:
        verbose_name_plural = 'Przeprowadzone szkolenia'

    def __str__(self):
        pass
