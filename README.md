# Cafe API

REST API project for a café: users, products, and orders. Implemented using Django, PostgreSQL, and Docker.

## Tech Stack

- Python 3.11  
- Django 5.2  
- Django REST Framework  
- PostgreSQL  
- Docker  


## Installation

1. Copy the repository. 
```bash
git clone https://github.com/karioczi/cafe_api.git
cd cafe_api
```
2. Create a '.env' file in the project root:
- Open the '.env.examples file', 
- Set your own password in the ‘DB_PASSWORD’ field 
- Copy all contents into the '.env' file.

3. Rebuild the image and start the container.
```bash
docker-compose up --build
```
4. Make migrations.
```bash
docker-compose exec web python manage.py migrate
```
5. (Optional) Create superuser.
```bash
docker-compose exec web python manage.py createsuperuser
```