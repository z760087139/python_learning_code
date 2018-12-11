# write in pools/models.py

from django.db import models
class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')


# app the models
# in mysite/setting.py
# INSTALLED_APPS= [
#   'polls.apps.PollsConfig
# ]

# then use the manage.py command
# python manage.py makemigrations polls

# check the file in polls/migraions:
# python manage.py sqlmigrate polls 0001

# create tables:
# python manage.py migrate



