import pytest #type:ignore 
from rest_framework import status #type:ignore
from rest_framework.test import APIClient #type:ignore
from django.contrib.auth import get_user_model
from products.models import Product

User = get_user_model()

@pytest.fixture
def admin_user(db):
    return User.objects.create_user(username='admin', password='pass', is_staff=True)

@pytest.fixture
def normal_user(db):
    return User.objects.create_user(username='user', password='pass')

@pytest.fixture
def auth_client_admin(admin_user):
    client = APIClient()
    client.login(username='admin', password='pass')
    return client

@pytest.fixture
def auth_client_user(normal_user):
    client = APIClient()
    client.login(username='user', password='pass')
    return client

@pytest.mark.django_db
def test_product_list():
    Product.objects.create(name='Product1', price=10.0)
    client = APIClient()
    response = client.get('/api/products/')
    assert response.status_code == 200
    assert len(response.data) == 1

@pytest.mark.django_db
def test_product_create_by_admin(auth_client_admin):
    data = {'name': 'New Product', 'price': 25.5}
    response = auth_client_admin.post('/api/products/', data, format='json')
    assert response.status_code == status.HTTP_201_CREATED

@pytest.mark.django_db
def test_product_create_by_user(auth_client_user):
    data = {'name': 'Fail Product', 'price': 20.0}
    response = auth_client_user.post('/api/products/', data, format='json')
    assert response.status_code == status.HTTP_403_FORBIDDEN

@pytest.mark.django_db
def test_peoduct_detail():
    product = Product.objects.create(name='Detail Product', price=5.0)
    client = APIClient()
    response = client.get(f'/api/products/{product.id}/', format='json')
    assert response.status_code == 200
    assert response.data['name'] == 'Detail Product'

@pytest.mark.django_db
def test_product_update_by_admin(auth_client_admin):
    product = Product.objects.create(name='Old', price=10.0)
    response = auth_client_admin.patch(f'/api/products/{product.id}/', {'name': 'Updated'}, format='json')
    assert response.status_code == 200
    assert response.data['name'] == 'Updated'

@pytest.mark.django_db
def test_product_update_by_user(auth_client_user):
    product = Product.objects.create(name='Old', price=10.0)
    response = auth_client_user.patch(f'/api/products/{product.id}/', {'name': 'Updated'}, format='json')
    assert response.status_code == 403

@pytest.mark.django_db
def test_product_delete_by_admin(auth_client_admin):
    product = Product.objects.create(name='ToDelete', price=10.0)
    response = auth_client_admin.delete(f'/api/products/{product.id}/', format='json')
    assert response.status_code == 204

@pytest.mark.django_db
def test_product_delete_by_user(auth_client_user):
    product = Product.objects.create(name='ToDelete', price=10.0)
    response = auth_client_user.delete(f'/api/products/{product.id}/', format='json')
    assert response.status_code == 403