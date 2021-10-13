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
    phone = models.PositiveIntegerField()
    level = models.SmallIntegerField(choices=LEVELS, default=-1)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return f'{self.user.first_name} {self.user.last_name}, kom. {self.phone}'


class TrainerTimetable(models.Model):

    # Dostępny czas pracy trenera w sezonie - wskazanie, w które dni, w jakich godzinach

    trainer_id = models.ForeignKey(Trainer, on_delete=models.CASCADE)
    season = models.SmallIntegerField(choices=SEASONS, default=0)
    day = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField()

    def __str__(self):
        return f'{self.trainer_id.user.first_name} {self.trainer_id.user.last_name}'


class TrainerBilling(models.Model):

    # Rozliczenie czasu pracy trenera: czas poświęcony na treningi i czas, za który trener otrzymał wynagrodzenie

    trainer_id = models.ForeignKey(Trainer, on_delete=models.CASCADE)
    season = models.SmallIntegerField(choices=SEASONS, default=0)
    hours_completed = models.PositiveSmallIntegerField(default=0)
    hours_paid = models.PositiveSmallIntegerField(default=0)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)


class TrainingPacket(models.Model):

    # Pakiety treningowe, które może wykupić kursant

    name = models.CharField(max_length=50)
    season = models.SmallIntegerField(choices=SEASONS, default=0)
    number_of_hours = models.PositiveSmallIntegerField()
    price = models.PositiveSmallIntegerField()
    active = models.BooleanField(default=False)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return f'sezon: {self.season}, nazwa: {self.name}'


class Student(models.Model):
    user = models.OneToOneField(User, models.SET_NULL, null=True, blank=True)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.EmailField(null=True, blank=True)
    phone = models.PositiveIntegerField()
    weight = models.SmallIntegerField(null=True, blank=True)
    height = models.SmallIntegerField(null=True, blank=True)
    consents = models.BooleanField(default=False)
    available_hours = models.SmallIntegerField(default=0)
    used_hours = models.SmallIntegerField(default=0)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return f'{self.first_name} {self.last_name}, kom. {self.phone}'


# class Consent(models.Model):
#     name = models.CharField(max_length=256)
#     description = models.TextField()
#     date_of_signing = models.DateTimeField() # powinno byc w modelu pośrednim
#     student_id = models.ManyToManyField(Student)


class Booking(models.Model):

    # Rezerwacja szkolenia: jeden instruktor, jeden lub wielu kursantów

    start_time = models.DateTimeField()
    duration = models.PositiveSmallIntegerField(default=1)
    trainer_id = models.ForeignKey(Trainer, on_delete=models.CASCADE)
    students = models.ManyToManyField(Student)
    cancellation = models.BooleanField(default=False)
    description = models.TextField(null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)


class Training(models.Model):
    booking_id = models.OneToOneField(Booking, on_delete=models.CASCADE)
    start_time = models.DateTimeField()
    duration = models.PositiveSmallIntegerField(default=1)
    trainer_id = models.ForeignKey(Trainer, on_delete=models.CASCADE)
    students = models.ManyToManyField(Student, through="StudentTraining")
    acceptance = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.trainer_id.user.first_name} {self.trainer_id.user.last_name}, {self.start_time} {self.duration}h'


class StudentTraining(models.Model):

    # Model pośredni między Student i Training
    # Przechowuje liczbę godzin poświęconych przez konkretnego kursanta na konkretny trening
    # Czas poświęcony na wspólny trening może okazać się różny dla każdego kursanta (np. kontuzja w trakcie treningu)
    # Terning może trwać inną długość czasu niż zaplanowano w rezerwacji (np. z powodu warunków pogodowych)

    student_id = models.ForeignKey(Student, on_delete=models.CASCADE)
    training_id = models.ForeignKey(Training, on_delete=models.CASCADE)
    duration = models.PositiveSmallIntegerField(default=0)
    description = models.TextField(null=True, blank=True)
