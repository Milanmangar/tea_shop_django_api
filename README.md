# Think_bride_python_django_api

python-django rest api for tea shop

**How to run the project**

1) cd tea_shop_django_rest
2) pip install -r requirements.txt
3) install postgresql
4) python manage.py migrate
5) python manage.py createsuperuser (fill in the you details)
6) python manage.py runserver 0.0.0.0:8000

**How to run the test**

1) cd tea_shop_django_rest
2) python manage.py test

URLS

(GET and POST) http://localhost:8000/api/items/

(GET, PUT, DELETE) http://localhost:8000/api/items/id_of_the_item_to_be_replaced_by_this
  
