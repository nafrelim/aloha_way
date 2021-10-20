import pytest
from django.contrib.auth.models import User

from .models import Trainer, TrainingPacket, Student, Booking, Training, StudentTraining


@pytest.fixture
def users():
    lst = []
    for x in range(10):
        lst.append(User.objects.create(username=str(x)))
    return lst


@pytest.fixture
def trainers(users):
    lst = []
    for x in range(10):
        lst.append(Trainer.objects.create(user=users[x], phone=x))
    return lst


@pytest.fixture
def packets():
    lst = []
    for x in range(10):
        lst.append(TrainingPacket.objects.create(name=x, number_of_hours=x, price=x))
    return lst


@pytest.fixture
def students():
    lst = []
    for x in range(10):
        lst.append(Student.objects.create(first_name=x, last_name=x, email='12@wp.pl', phone=123456))
    return lst


@pytest.fixture
def bookings(users, trainers, students):
    lst = []
    for x in range(10):
        if x == 9:
            break
        student1 = students[x]
        student2 = students[x+1]
        booking = Booking.objects.create(day='2021-10-20', start_time='14:00', duration=x, trainer=trainers[x])
        booking.students.add(student1)
        booking.students.add(student2)
        lst.append(booking)
    return lst


@pytest.fixture
def trainings(trainers, students, bookings):
    lst = []
    for x in range(10):
        if x == 9:
            break
        student1 = students[x]
        student2 = students[x+1]
        training = Training.objects.create(booking=bookings[x], day='2021-10-20', start_time='14:00',
                                           duration=x, trainer=trainers[x], acceptance=True)
        student_training1 = StudentTraining.objects.create(student=student1, training=trainings[x])
        student_training2 = StudentTraining.objects.create(student=student2, training=trainings[x+1])
        lst.append(training)
    return lst


@pytest.fixture
def student_trainings(trainers, students, bookings):
    lst = []
    for x in range(10):
        if x == 9:
            break
        student1 = students[x]
        student2 = students[x + 1]
        training = Training.objects.create(booking=bookings[x], day='2021-10-20', start_time='14:00',
                                           duration=x, trainer=trainers[x], acceptance=True)
        student_training1 = StudentTraining.objects.create(student=student1, training=trainings[x])
        student_training2 = StudentTraining.objects.create(student=student2, training=trainings[x+1])
        lst.append(student_training1)
        lst.append(student_training2)
    return lst
