from django.db import models
from django.contrib.auth.models import User

from aloha_way.project_settings import LEVELS, SEASONS


class Trainer(models.Model):
    """
    Model for trainers.
    """

    user = models.OneToOneField(User, primary_key=True, on_delete=models.CASCADE)
    phone = models.PositiveIntegerField(verbose_name='Numer telefonu')
    level = models.SmallIntegerField(choices=LEVELS, default=0, verbose_name='Poziom kompetencji')
    hours_completed = models.PositiveSmallIntegerField(default=0, verbose_name='Zrealizowanych godzin')
    active = models.BooleanField(default=True, verbose_name='Czy pracuje w tym sezonie?')
    description = models.TextField(null=True, blank=True, verbose_name='Dodatkowe informacje')

    class Meta:
        # ordering = ['user__last_name', 'user__first_name']
        verbose_name_plural = 'Instruktorzy'

    def __str__(self):
        return f'{self.user.last_name} {self.user.first_name}'


class TrainerTimetable(models.Model):
    """
    Model for storing trainer's timetable.
    Available working time of the trainer in the season - an indication of which days and hours.
    """

    trainer = models.ForeignKey(Trainer, on_delete=models.CASCADE)
    season = models.SmallIntegerField(choices=SEASONS, default=0, verbose_name='Sezon')
    day = models.DateField(verbose_name='Dzień')
    start_time = models.TimeField(verbose_name='Początek')
    end_time = models.TimeField(verbose_name='Koniec')

    class Meta:
        ordering = ['day', 'start_time']
        verbose_name_plural = 'Terminy instruktora'

    def __str__(self):
        return f'{self.trainer.user.first_name} {self.trainer.user.last_name}, {self.day} ' \
               f'{self.start_time}-{self.end_time}'


class Student(models.Model):
    """
    Model for students.
    """

    user = models.OneToOneField(User, models.SET_NULL, null=True, blank=True)
    first_name = models.CharField(max_length=150, verbose_name='Imię')
    last_name = models.CharField(max_length=150, verbose_name='Nazwisko')
    email = models.EmailField(null=True, blank=True, verbose_name='Email')
    phone = models.PositiveIntegerField(verbose_name='Numer telefonu')
    weight = models.SmallIntegerField(null=True, blank=True, verbose_name='Waga')
    height = models.SmallIntegerField(null=True, blank=True, verbose_name='Wzrost')
    consents = models.BooleanField(default=False, verbose_name='Podpisanie zgód')
    available_hours = models.SmallIntegerField(default=0, verbose_name='Dostępne godziny')
    used_hours = models.PositiveSmallIntegerField(default=0, verbose_name='Godziny wykorzystane')
    description = models.TextField(null=True, blank=True, verbose_name='Dodatkowe informacje')

    class Meta:
        ordering = ['last_name', 'first_name']
        verbose_name_plural = 'Kursanci'

    def __str__(self):
        return f'{self.last_name} {self.first_name}'


class Consent(models.Model):
    """
    Model for student's consents.
    """

    name = models.CharField(max_length=256)
    description = models.TextField()

    class Meta:
        ordering = ['name']
        verbose_name_plural = 'Wykaz zgód'

    def __str__(self):
        return f'{self.name}'


class StudentConsent(models.Model):
    """
    An intermediate model between Student and Consent
    It stores the consent information which the student has accepted
    """

    student = models.ForeignKey(Student, on_delete=models.CASCADE, verbose_name='Student')
    consent = models.ForeignKey(Consent, on_delete=models.CASCADE, verbose_name='Zgoda')
    decision = models.BooleanField(blank=True, default=False, verbose_name='Decyzja o zgodzie')

    class Meta:
        ordering = ['student__last_name', 'student__first_name']
        verbose_name_plural = 'Zgody kursantów'

    def __str__(self):
        return f'{self.student.last_name} {self.student.first_name}'
