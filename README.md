# Cafe API

Проект REST API для кафе: пользователи, продукты и заказы. Реализован на Django, PostgreSQL, Docker.

## Стек

- Python 3.11  
- Django 5.2  
- Django REST Framework  
- PostgreSQL  
- Docker  

## Установка

```bash
git clone https://github.com/karioczi/juniordown.git
cd juniordown
docker-compose up --build
docker-compose exec web python manage.py migrate
docker-compose exec web python manage.py createsuperuser  # опционально
