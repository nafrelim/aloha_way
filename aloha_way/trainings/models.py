from django.db import models
from django.contrib.auth.models import User
from people.models import Trainer, Student

# Poniższe słowniki docelowo powinny być tabelami

SEASONS = (
                (0, 2021),  # domyślny sezon
                (1, 2022),
             )


class TrainingPacket(models.Model):

    # Pakiety treningowe, które może wykupić kursant

    name = models.CharField(max_length=50, verbose_name='Nazwa')
    number_of_hours = models.PositiveSmallIntegerField(verbose_name='Liczba godzin')
    price = models.PositiveSmallIntegerField(verbose_name='Cena')
    active = models.BooleanField(default=False, verbose_name='Aktywny')
    description = models.TextField(null=True, blank=True, verbose_name='Dodatkowe informacje')

    class Meta:
        ordering = ['number_of_hours']

    def __str__(self):
        return f'{self.name}'


class Booking(models.Model):

    # Rezerwacja szkolenia: jeden instruktor, jeden lub wielu kursantów
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

    def __str__(self):
        d = self.day.strftime('%Y-%m-%d')
        h = self.start_time.strftime('%H:%M')
        return f'{self.trainer.user.last_name} {self.trainer.user.first_name}, start: {d} {h}, {self.duration} godz.'


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

    def __str__(self):
        d = self.day.strftime('%Y-%m-%d')
        h = self.start_time.strftime('%H:%M')
        return f'{self.trainer.user.last_name} {self.trainer.user.first_name}, start: {d}, {h}, {self.duration} godz.'


class StudentTraining(models.Model):

    # Model pośredni między Student i Training
    # Przechowuje liczbę godzin poświęconych przez konkretnego kursanta na konkretny trening
    # Czas poświęcony na wspólny trening może okazać się różny dla każdego kursanta (np. kontuzja w trakcie treningu)
    # Terning może trwać inną długość czasu niż zaplanowano w rezerwacji (np. z powodu warunków pogodowych)

    student = models.ForeignKey(Student, on_delete=models.CASCADE, verbose_name='Instruktor')
    training = models.ForeignKey(Training, on_delete=models.CASCADE, verbose_name='Trening')
    duration = models.PositiveSmallIntegerField(default=0, verbose_name='Czas trwania')
    description = models.TextField(null=True, blank=True, verbose_name='Dodatkowe informacje')
