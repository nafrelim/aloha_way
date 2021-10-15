from django.db import models
from django.contrib.auth.models import User

# Poniższe słowniki docelowo powinny być tabelami

LEVELS = (
                (-1, 'not defined'),
                (0, 'junior'),
                (1, 'mid'),
                (2, 'senior'),
             )


SEASONS = (
                (0, 2021),  # domyślny sezon
                (1, 2022),
             )


class Trainer(models.Model):
    user = models.OneToOneField(User, primary_key=True, on_delete=models.CASCADE)
    phone = models.PositiveIntegerField(verbose_name='Numer telefonu')
    level = models.SmallIntegerField(choices=LEVELS, default=-1, verbose_name='Poziom kompetencji')
    description = models.TextField(null=True, blank=True, verbose_name='Dodatkowe informacje')

    def __str__(self):
        return f'{self.user.first_name} {self.user.last_name}, kom. {self.phone}'


class TrainerTimetable(models.Model):

    # Dostępny czas pracy trenera w sezonie - wskazanie, w które dni, w jakich godzinach

    trainer_id = models.ForeignKey(Trainer, on_delete=models.CASCADE)
    season = models.SmallIntegerField(choices=SEASONS, default=0, verbose_name='Sezon')
    day = models.DateField(verbose_name='Dzień')
    start_time = models.TimeField(verbose_name='Początek')
    end_time = models.TimeField(verbose_name='Koniec')

    def __str__(self):
        return f'{self.trainer_id.user.first_name} {self.trainer_id.user.last_name}'


class TrainerBilling(models.Model):

    # Rozliczenie czasu pracy trenera: czas poświęcony na treningi i czas, za który trener otrzymał wynagrodzenie

    trainer_id = models.ForeignKey(Trainer, on_delete=models.CASCADE)
    season = models.SmallIntegerField(choices=SEASONS, default=0, verbose_name='Sezon')
    hours_completed = models.PositiveSmallIntegerField(default=0, verbose_name='Zrealizowanych godzin')
    hours_paid = models.PositiveSmallIntegerField(default=0, verbose_name='Godziny opłacone')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'Sezon: {self.season}, godz. zrealizowane: {self.hours_completed}, godz. opłacone: {self.hours_paid}'


class TrainingPacket(models.Model):

    # Pakiety treningowe, które może wykupić kursant

    name = models.CharField(max_length=50, verbose_name='Nazwa')
    season = models.SmallIntegerField(choices=SEASONS, default=0, verbose_name='Sezon')
    number_of_hours = models.PositiveSmallIntegerField(verbose_name='Liczba godzin')
    price = models.PositiveSmallIntegerField(verbose_name='Cena')
    active = models.BooleanField(default=False, verbose_name='Aktywny')
    description = models.TextField(null=True, blank=True, verbose_name='Dodatkowe informacje')

    def __str__(self):
        return f'sezon: {self.season}, nazwa: {self.name}'


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
    used_hours = models.SmallIntegerField(default=0, verbose_name='Godziny wykorzystane')
    description = models.TextField(null=True, blank=True, verbose_name='Dodatkowe informacje')

    def __str__(self):
        return f'{self.first_name} {self.last_name}, kom. {self.phone}'


# class Consent(models.Model):
#     name = models.CharField(max_length=256)
#     description = models.TextField()
#     date_of_signing = models.DateTimeField() # powinno byc w modelu pośrednim
#     student_id = models.ManyToManyField(Student)


class Booking(models.Model):

    # Rezerwacja szkolenia: jeden instruktor, jeden lub wielu kursantów

    start_time = models.DateTimeField(verbose_name='Godzina rozpoczęcia')
    duration = models.PositiveSmallIntegerField(default=1, verbose_name='Czas trwania(godz)')
    trainer_id = models.ForeignKey(Trainer, on_delete=models.CASCADE, verbose_name='Instruktor')
    students = models.ManyToManyField(Student, verbose_name='Kursant')
    cancellation = models.BooleanField(default=False, verbose_name='Skasowanie')
    description = models.TextField(null=True, blank=True, verbose_name='Dodatkowe informacje')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'Instruktor: {self.trainer_id}, star: {self.start_time}, czas trwania: {self.duration}'


class Training(models.Model):
    booking_id = models.OneToOneField(Booking, on_delete=models.CASCADE, verbose_name='Rezerwacja')
    start_time = models.DateTimeField(verbose_name='Godzina rozpoczęcia')
    duration = models.PositiveSmallIntegerField(default=1, verbose_name='Czas trwania(godz)')
    trainer_id = models.ForeignKey(Trainer, on_delete=models.CASCADE, verbose_name='Instruktor')
    students = models.ManyToManyField(Student, through="StudentTraining", verbose_name='Kursanci')
    acceptance = models.BooleanField(default=False, verbose_name='Akceptacja')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.trainer_id.user.first_name} {self.trainer_id.user.last_name}, {self.start_time} {self.duration}h'


class StudentTraining(models.Model):

    # Model pośredni między Student i Training
    # Przechowuje liczbę godzin poświęconych przez konkretnego kursanta na konkretny trening
    # Czas poświęcony na wspólny trening może okazać się różny dla każdego kursanta (np. kontuzja w trakcie treningu)
    # Terning może trwać inną długość czasu niż zaplanowano w rezerwacji (np. z powodu warunków pogodowych)

    student_id = models.ForeignKey(Student, on_delete=models.CASCADE, verbose_name='Instruktor')
    training_id = models.ForeignKey(Training, on_delete=models.CASCADE, verbose_name='Trening')
    duration = models.PositiveSmallIntegerField(default=0, verbose_name='Czas trwania')
    description = models.TextField(null=True, blank=True, verbose_name='Dodatkowe informacje')
