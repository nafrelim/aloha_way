import pytest
from django.test import TestCase, Client
from django.urls import reverse


def test_empty():
    client = Client()
    response = client.get(reverse("index_view"))
    assert response.status_code == 200


def test_empty_post():
    client = Client()
    response = client.post(reverse("index_view"))
    assert response.status_code == 405


@pytest.mark.django_db
def test_create_users(users):
    for user in users:
        assert user in users


@pytest.mark.django_db
def test_trainers_list_get():
    client = Client()
    response = client.get(reverse("trainers_list_view"))
    assert response.status_code == 200
    trainers_list = response.context['object_list']
    assert trainers_list.count() == 0


@pytest.mark.django_db
def test_trainer_list_get_not_empty(trainers):
    client = Client()
    response = client.get(reverse("trainers_list_view"))
    assert response.status_code == 200
    trainers_list = response.context['object_list']
    assert trainers_list.count() == len(trainers)
    for trainer in trainers:
        assert trainer in trainers_list


@pytest.mark.django_db
def test_packets_list_get_not_empty(packets):
    client = Client()
    response = client.get(reverse("packets_list_view"))
    assert response.status_code == 200
    packets_list = response.context['object_list']
    assert packets_list.count() == len(packets)
    for packet in packets:
        assert packet in packets_list


@pytest.mark.django_db
def test_students_list_get_not_empty(students):
    client = Client()
    response = client.get(reverse("students_list_view"))
    assert response.status_code == 200
    students_list = response.context['object_list']
    assert students_list.count() == len(students)
    for student in students:
        assert student in students_list


@pytest.mark.django_db
def test_bookings_list_get_not_empty(bookings):
    client = Client()
    response = client.get(reverse("bookings_list_view"))
    assert response.status_code == 200
    bookings_list = response.context['object_list']
    assert bookings_list.count() == len(bookings)
    for booking in bookings:
        assert booking in bookings_list


@pytest.mark.django_db
def test_trainings_list_get_not_empty(trainings):
    client = Client()
    response = client.get(reverse("trainings_list_view"))
    assert response.status_code == 200
    trainings_list = response.context['object_list']
    assert trainings_list.count() == len(trainings)
    for training in trainings:
        assert training in trainings_list


@pytest.mark.django_db
def test_student_trainings_list_get_not_empty(student_trainings):
    client = Client()
    response = client.get(reverse("training_student_view"))
    assert response.status_code == 200
    student_trainings_list = response.context['object_list']
    assert student_trainings_list.count() == len(student_trainings)
    for student_training in student_trainings:
        assert student_training in student_trainings_list
