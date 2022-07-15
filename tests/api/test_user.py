import pytest
from django.test import client
from django.urls import reverse
from django.utils import timezone
from rest_framework.response import Response
from rest_framework.test import APIClient
from base.models import Product, Order
from django.contrib.auth.models import User

client = APIClient()

'''
Unit tests 
'''

def test_user_creation(new_user):
    count = User.objects.all().count()
    assert count == 1


def test_superuser_creation(new_superuser):
    count = User.objects.all().count()
    assert count == 1


def test_user_creation1(new_user):
    assert isinstance(new_user, User) is True


def test_superuser_details(new_superuser):
    assert new_superuser.is_staff
    assert new_superuser.is_superuser
    assert new_superuser.is_active
    assert new_superuser.username == "test@test.com"
    assert new_superuser.first_name == "test_name"
    assert new_superuser.last_name == "lastname"
    assert new_superuser.email == "test@test.com"


def test_user_details(new_user):
    assert new_user.is_staff is False
    assert new_user.is_superuser is False
    assert new_user.is_active
    assert new_user.username == "test@test.com"
    assert new_user.first_name == "test_name"
    assert new_user.last_name == "lastname"
    assert new_user.email == "test@test.com"


def test_set_check_password_user(new_user):
    new_user.set_password("new-password")
    assert new_user.check_password("new-password") is True


def test_set_check_password_superuser(new_superuser):
    new_superuser.set_password("new-password")
    assert new_superuser.check_password("new-password") is True


def test_delete_user(new_user):
    User.delete(new_user)
    count = User.objects.all().count()
    assert count == 0

def test_delete_superuser(new_superuser):
    User.delete(new_superuser)
    count = User.objects.all().count()
    assert count == 0




'''
Integration tests
'''


@pytest.mark.django_db
def test_register_user():
    payload = dict(
        name="testing123",
        email="test11@test.com",
        password="super-secret"
    )

    response = client.post("/api/users/register/", payload)

    data = response.data

    assert data["name"] == payload["name"]
    assert data["username"] == payload["email"]
    assert "password" not in data


@pytest.mark.django_db
def test_login_user():
    payload = dict(
        name="testing123",
        email="test11@test.com",
        password="super-secret"
    )
    client.post("/api/users/register/", payload)
    response = client.post("/api/users/login/", dict(username="test11@test.com", password="super-secret"))
    assert response.status_code == 200


@pytest.mark.django_db
def test_login_user_fail():
    response = client.post("/api/users/login/", dict(username="test11@test.com", password="super-secret"))
    assert response.status_code == 401


@pytest.mark.django_db
def test_get_me():
    payload = dict(
        name="testing123",
        email="test111@test.com",
        password="super-secret"
    )

    client.post("/api/users/register/", payload)
    client.post("/api/users/login/", dict(username="test111@test.com", password="super-secret"))
    response = client.get("/api/users/profile/")
    assert response.status_code == 200
    # data = response.data
    # assert data["name"] == "testing123"


@pytest.mark.django_db
def test_logout():
    payload = dict(
        name="testing123",
        email="test111@test.com",
        password="super-secret"
    )

    client.post("/api/users/register/", payload)
    client.post("/api/users/login/", dict(username="test111@test.com", password="super-secret"))
    response = client.post("/api/users/logout/")
    assert response.status_code == 200
