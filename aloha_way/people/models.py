from django.db import models
from django.contrib.auth.models import User

# Create your models here.
LEVELS = (
                (0, 'nieokreślony'),
                (1, 'junior'),
                (2, 'mid'),
                (3, 'senior'),
             )


class Trainer(models.Model):
    user = models.OneToOneField(User, primary_key=True, on_delete=models.CASCADE)
    phone = models.PositiveIntegerField(verbose_name='Numer telefonu')
    level = models.SmallIntegerField(choices=LEVELS, default=0, verbose_name='Poziom kompetencji')
    hours_completed = models.PositiveSmallIntegerField(default=0, verbose_name='Zrealizowanych godzin')
    active = models.BooleanField(default=True, verbose_name='Czy pracuje w tym sezonie?')
    description = models.TextField(null=True, blank=True, verbose_name='Dodatkowe informacje')

    def __str__(self):
        return f'{self.user.last_name} {self.user.first_name}'


# class TrainerTimetable(models.Model):
#
#     # Dostępny czas pracy trenera w sezonie - wskazanie, w które dni, w jakich godzinach
#
#     trainer = models.ForeignKey(Trainer, on_delete=models.CASCADE)
#     season = models.SmallIntegerField(choices=SEASONS, default=0, verbose_name='Sezon')
#     day = models.DateField(verbose_name='Dzień')
#     start_time = models.TimeField(verbose_name='Początek')
#     end_time = models.TimeField(verbose_name='Koniec')
#
#     class Meta:
#         ordering = ['day', 'start_time']
#
#     def __str__(self):
#         return f'{self.trainer.user.first_name} {self.trainer.user.last_name}, {self.day} ' \
#                f'{self.start_time}-{self.end_time}'


class Student(models.Model):
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
        ordering = ['last_name']

    def __str__(self):
        return f'{self.last_name} {self.first_name}'


# class Consent(models.Model):
#     name = models.CharField(max_length=256)
#     description = models.TextField()
#     date_of_signing = models.DateTimeField() # powinno byc w modelu pośrednim
#     student_id = models.ManyToManyField(Student)

