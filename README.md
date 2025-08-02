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
4. Make migrations. The server must be running during migrations. Open another terminal window and write command below.
```bash
docker-compose exec web python manage.py migrate
```
5. (Optional) Create superuser.
```bash
docker-compose exec web python manage.py createsuperuser
```
If the server starts successfully, it will be accessible at http://127.0.0.1:8000/api/docs/

## Endpoint check

1. Open browser and go to http://127.0.0.1:8000/api/docs/

2. Registration:
- In the “Users” API section, find the /api/users/registration/ endpoint; 
- In right corner of endpoint window, find "Try it out";
- Enter your own data or use the ready-made ones in registration fields;

3. Receiving authorization tokens:
- After successful registration you receive 201 response code; 
- Find /api/users/login/ in the same API section; 
- In right corner of endpoint window find "Try it out"; 
- If you use the provided data, just click "Execute", otherwise enter your own data as in the "registration" endpoint;
- After successful authorization you receive "access" and "refresh" tokens in the field below. 
- Copy "access" token without "";

4. Authorization:
- Go to the top of the page and find "Authorize" button;
- Push it, and provide "access" token in "value" field; 
- Again, push "Authorize" button below;


 
