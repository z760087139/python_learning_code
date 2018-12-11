# create a superuser
# python manage.py createsuperuser

# then  input the username
# Username: admin

# email:
# Email address: ....

# password *2

# admin page:
# .../admin

# to add class in admin page to manage  like polls Questions

# polls/admin.py
from django.contrib import admin
from .models import Question
admin.site.register(Question)