# Django-Celery app
Manages large workloads but setting up workers and queues.

- Create conda environment with Django
```
conda create -n djangocelery python=3.10.4
```
```
conda activate djangocelery
```
```
pip install Django==4.0.5
```

- Start Django project
```
django-admin startproject djcel
```

- Start Django app
```
python manage.py startapp worker
```

- Create one view following https://docs.djangoproject.com/en/4.0/intro/tutorial01/

- Install Celery
```
pip install celery==5.2.7
```

- Create Celery app following https://docs.celeryq.dev/en/latest/django/first-steps-with-django.html

- Install Redis to have a server
``` 
pip install redis==4.3.3
```

- Run task asynchorously following https://www.youtube.com/watch?v=IcuteHZJlHE
