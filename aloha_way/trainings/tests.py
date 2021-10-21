import pytest
from django.test import Client
from django.urls import reverse

from trainings.models import Student


def test_empty():
    client = Client()
    response = client.get(reverse('index_view'))
    assert response.status_code == 200


def test_empty_post():
    client = Client()
    response = client.post(reverse('index_view'))
    assert response.status_code == 405


@pytest.mark.django_db
def test_trainers_list_get(user):
    client = Client()
    client.force_login(user)
    response = client.get(reverse('trainers_list_view'))
    assert response.status_code == 200
    trainers_list = response.context['object_list']
    assert trainers_list.count() == 0


@pytest.mark.django_db
def test_trainer_list_get_not_empty(user, trainers):
    client = Client()
    client.force_login(user)
    response = client.get(reverse('trainers_list_view'))
    assert response.status_code == 200
    trainers_list = response.context['object_list']
    assert trainers_list.count() == len(trainers)
    for trainer in trainers:
        assert trainer in trainers_list


@pytest.mark.django_db
def test_trainer_detail_get_login(user, trainer):
    client = Client()
    client.force_login(user)
    response = client.get(reverse('trainer_detail_view', args=[trainer.pk]))
    assert response.status_code == 200


@pytest.mark.django_db
def test_trainer_add_get_not_login():
    client = Client()
    response = client.get(reverse('trainer_add_view'))
    assert response.status_code == 302


@pytest.mark.django_db
def test_trainer_add_get_login(user):
    client = Client()
    client.force_login(user)
    trainer = {
        'user': user,
        'phone': 12345
    }
    response = client.post(reverse('trainer_add_view'), data=trainer)
    assert response.status_code == 200


@pytest.mark.django_db
def test_trainer_update_get_login(user, trainer):
    client = Client()
    client.force_login(user)
    response = client.post(reverse('trainer_update_view', args=[trainer.pk]), data={'phone': 54321})
    assert response.status_code == 200
    item = response.context['object']
    assert item.phone != trainer.phone


@pytest.mark.django_db
def test_students_list_not_permissions(user, students):
    client = Client()
    client.force_login(user)
    response = client.get(reverse('students_list_view'))
    assert response.status_code == 403


@pytest.mark.django_db
def test_students_list_get_not_empty_with_permissions(superuser, students):
    client = Client()
    client.force_login(superuser)
    response = client.get(reverse('students_list_view'))
    assert response.status_code == 200
    students_list = response.context['object_list']
    assert students_list.count() == len(students)
    for student in students:
        assert student in students_list


@pytest.mark.django_db
def test_student_detail_get_login(user, student):
    client = Client()
    client.force_login(user)
    response = client.get(reverse('student_detail_view', args=[student.pk]))
    assert response.status_code == 200


@pytest.mark.django_db
def test_student_add_get_not_login():
    client = Client()
    response = client.get(reverse('student_add_view'))
    assert response.status_code == 302


@pytest.mark.django_db
def test_student_add_get_login(user):
    client = Client()
    client.force_login(user)
    student = {
        'first_name':'Zenon',
        'last_name':'Zieliński',
        'email':'12@wp.pl',
        'phone':123456
    }
    response = client.post(reverse('student_add_view'), data=student)
    assert response.status_code == 200


@pytest.mark.django_db
def test_student_update_get_login(user, student):
    client = Client()
    client.force_login(user)
    response = client.post(reverse('student_update_view', args=[student.pk]), data={'phone': 54321})
    assert response.status_code == 200
    item = response.context['object']
    assert item.phone != student.phone


@pytest.mark.django_db
def test_packets_list_get_not_empty(user, packets):
    client = Client()
    client.force_login(user)
    response = client.get(reverse('packets_list_view'))
    assert response.status_code == 200
    packets_list = response.context['object_list']
    assert packets_list.count() == len(packets)
    for packet in packets:
        assert packet in packets_list


@pytest.mark.django_db
def test_packet_detail_get_login(user, packet):
    client = Client()
    client.force_login(user)
    response = client.get(reverse('packet_detail_view', args=[packet.pk]))
    assert response.status_code == 200


@pytest.mark.django_db
def test_packet_add_get_login(user):
    client = Client()
    client.force_login(user)
    packet = {
        'name': 'test',
        'number_of_hours': 10,
        'price': 2000
    }
    response = client.post(reverse('packet_add_view'), data=packet)
    assert response.status_code == 302


@pytest.mark.django_db
def test_packet_add_for_student_get_login(user, student):
    client = Client()
    client.force_login(user)
    packet = {
        'name': 'test',
        'number_of_hours': 10,
        'price': 2000
    }
    response = client.post(reverse('packet_add_for_student_view', args=[student.pk]), data=packet)
    # trochę słabe - jak sprawdzić czu u studenta się zwiększyło?
    assert response.status_code == 302


@pytest.mark.django_db
def test_package_update_get_login(user, packet):
    client = Client()
    client.force_login(user)
    response = client.post(reverse('packet_update_view', args=[packet.pk]), data={'number_of_hours': 20})
    assert response.status_code == 200
    item = response.context['object']
    assert item.number_of_hours != packet.number_of_hours


@pytest.mark.django_db
def test_bookings_list_get_not_empty(bookings, user):
    client = Client()
    client.force_login(user)
    response = client.get(reverse('bookings_list_view'))
    assert response.status_code == 200
    bookings_list = response.context['object_list']
    assert bookings_list.count() == len(bookings)
    for booking in bookings:
        assert booking in bookings_list


@pytest.mark.django_db
def test_cancelled_bookings_list_get_not_empty(cancelled_bookings, user):
    client = Client()
    client.force_login(user)
    response = client.get(reverse('cancelled_bookings_list_view'))
    assert response.status_code == 200
    bookings_list = response.context['object_list']
    assert bookings_list.count() == len(cancelled_bookings)
    for booking in cancelled_bookings:
        assert booking in bookings_list


@pytest.mark.django_db
def test_booking_detail_get_login(user, booking):
    client = Client()
    client.force_login(user)
    response = client.get(reverse('booking_detail_view', args=[booking.pk]))
    assert response.status_code == 200


@pytest.mark.django_db
def test_booking_add_get_not_login():
    client = Client()
    response = client.get(reverse('student_add_view'))
    assert response.status_code == 302


@pytest.mark.django_db
def test_booking_add_get_login(user):
    client = Client()
    client.force_login(user)
    student = {
        'first_name':'Zenon',
        'last_name':'Zieliński',
        'email':'12@wp.pl',
        'phone':123456
    }
    response = client.post(reverse('student_add_view'), data=student)
    assert response.status_code == 200


@pytest.mark.django_db
def test_booking_update_get_login(user, student):
    client = Client()
    client.force_login(user)
    response = client.post(reverse('student_update_view', args=[student.pk]), data={'phone': 54321})
    assert response.status_code == 200
    item = response.context['object']
    assert item.phone != student.phone


@pytest.mark.django_db
def test_trainings_list_get_not_empty(trainings, user):
    client = Client()
    client.force_login(user)
    response = client.get(reverse('trainings_list_view'))
    assert response.status_code == 200
    trainings_list = response.context['object_list']
    assert trainings_list.count() == len(trainings)
    for training in trainings:
        assert training in trainings_list


@pytest.mark.django_db
def test_student_trainings_list_get_not_empty(student_trainings, user):
    client = Client()
    client.force_login(user)
    response = client.get(reverse('training_student_add_view'))
    assert response.status_code == 200
    studenttrainings_list = response.context['object_list']
    assert studenttrainings_list.count() == len(student_trainings)
    for student_training in student_trainings:
        assert student_training in studenttrainings_list
