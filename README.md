# Cafe API

REST API project for a café: users, products, and orders. Implemented using Django, PostgreSQL, and Docker.

## Tech Stack

- Python 3.11  
- Django 5.2  
- Django REST Framework  
- PostgreSQL  
- Docker  


## Installation

Copy the repository to a convenient folder. 
```bash
git clone https://github.com/karioczi/cafe_api.git
cd cafe_api
```
Create an '.env' file in the root directory of the project.
Open the '.env.examples file', set your password for the database in the ‘DB_PASSWORD’ field and copy all of its contents into the '.env' file.
Rebuild the image and start the container.
```bash
docker-compose up --build
```
Make migrations
```bash
docker-compose exec web python manage.py migrate
```
You can also create a superuser (optionally).
```bash
docker-compose exec web python manage.py createsuperuser
```