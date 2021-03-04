# REST-crud
CRUD operations using Django REST Framework

<br>


## Requirements
- Python 3
- Django 3
- Django Rest Framework

<br>

## Quick Setup

Clone repository

    git clone https://github.com/mr-engin3er/REST-crud.git

Go to directory

    cd REST-crud

Create virtual environment

    python3 -m venv env

Activate virtual environment

    source ./env/bin/activate

Install requirements

    pip install -r requirements.pip

Migrate database

    python manage.py migrate

Start Development server

    python manage.py runserver

<br>

## Repository tree
    REST_crud
        |-- __init__.py
        |-- asgi.py
        |-- settings.py
        |-- urls.py
        |-- wsgi.py
    crud
        |-- __init__.py
        |-- admin.py
        |-- api
            |   |-- __init__.py
            |   |-- serializers.py
            |   |-- views.py
        |-- apps.py
        |-- migrations
            |   |-- 0001_initial.py
            |   |-- __init__.py
        |-- models.py
        |-- tests.py
        |-- urls.py
        |-- views.py
    .gitignore
    README.md
    manage.py
    requirements.pip


Now all the API's is available on http://127.0.0.1:8000/

We can test all API's on any REST client(eg.- Postman)

<br>

## Available API endpoints

List all employee(GET)

```python
http://127.0.0.1:8000/
``` 

Create single employee(POST) 

```python
url: http://127.0.0.1:8000/create/ 
body: {"name": "","age": 15,"city": ""}
```


Detail of single employee(GET) 

```python
http://127.0.0.1:8000/detail/<int:id>
``` 

Update single employee(PUT) 

```python
url: http://127.0.0.1:8000/update/<int:id>
body: {"name": "","age": 15,"city": ""}
```


Delete single employee(DELETE) 

```python
http://127.0.0.1:8000/delete/<int:id>
``` 


   
Employee model

    cat ./crud/models.py

API views

    cat ./crud/api/views.py

Serializer

    cat ./crud/api/serializers.py

Unit testing using Django TestCases

    cat ./crud/tests.py