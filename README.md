# Think_bride_python_django_api

python-django rest api for tea shop

**How to run the project**

1) cd tea_shop_django_rest
2) pip install -r requirements.txt
3) install postgresql
4) set environment variable for DB credentials,DEBUG, SECRET_KEY(sent on mail) and add in settings.py
5) python manage.py migrate
6) python manage.py runserver

**How to run the test**

1) cd tea_shop_django_rest
2) python manage.py test

URLS

(GET and POST) http://localhost:8000/api/items/

(GET) http://localhost:8000/api/items/<pk>
  
  **Note: have sent settings.py file in mail if you want do not want to set environment varible, only DB credentials have to be set(credentials to be set sent on mail)
