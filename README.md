
## This project is a application built using Django (backend).

## Project Setup Instructions
### Backend (Django) Setup
* Clone the repository

* git clone https://github.com/uniquedeveloper143/iFoutDemoTest.git
* cd your-project/DemoTest

## Create and activate a virtual environment

* python -m venv env
* source env/bin/activate    # On Windows: env\Scripts\activate

## Install the required dependencies

* pip install -r requirements.txt

## Configure Environment Variables
* Create a .env file inside the backend directory and add your config/settings/.env:

## setup .env file 
* SECRET_KEY=
* API_KEY_SECRET=
* PROJECT_FULL_NAME=demo_test
* DEV_ADMIN_EMAIL=nafees.mohd@neosoftmail.com
* DB_NAME=demo_db
* DB_USER=root
* DB_PASSWORD=
* DB_HOST=127.0.0.1
* DB_PORT=3306

## Run migrations
* python manage.py migrate

## Create a superuser
* python manage.py createsuperuser

## Run the Django development server
*  manage.py runserver


## For API test you need to pass API_KEY and Token:

* login using username and password, you can get token in response
* pass the api-key and token in the header like:
* api-key: f9e068f7c25ec2eaf0fbed9f16a015460e06865ca22ec4a12a459172a96bc6f4
* token: token 8e476280-1b46-4d07-a86e-4f0ddf3c597b 

