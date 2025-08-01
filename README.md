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
If the server starts successfully, it will be accessible at http://127.0.0.1:8000/api/docs/

## Endpoint check

1. Go to http://127.0.0.1:8000/api/docs/

2. In the “Users” API section, find the /api/users/registration/ endpoint. In right corner of endpoint window find "Try it out". 
   Enter your own data or use the ready-made ones in registration fields

3. After succesfull registration, find /api/users/login/ in the same API section. In right corner of endpoint window find "Try it out". If you use the provided data, just click "Execute"; otherwise, enter your own data as in the "registration" endpoint.

4. After succesfull sing in you recieve "access" and "refresh" tokens in the field below
5. Then go to the top of the page and fint "Authorize" button, push it and provide "access" token in "value" field and again push "Authorize" button below


 
