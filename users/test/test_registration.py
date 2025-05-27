import pytest #type:ignore
from django.urls import reverse
from rest_framework import status #type:ignore
from rest_framework.test import APIClient #type:ignore
from django.contrib.auth import get_user_model

User = get_user_model()

@pytest.mark.django_db
def test_successful_registration():
    client = APIClient()
    url = reverse("registration")  # проверь name в urls.py
    data = {
        'username': 'testuser', 
        'email': 'test@example.com',
        'password': 'StrongPass123!',
        'password_confirm': 'StrongPass123!'
    }
    response = client.post(url, data, format='json')

    assert response.status_code == status.HTTP_201_CREATED
    assert User.objects.filter(email="test@example.com").exists()
