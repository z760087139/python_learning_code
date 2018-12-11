# dir :
# mysite/
#     manage.py
#     mysite/
#         __init__.py
#         settings.py
#         urls.py
#         wsgi.py
#     polls/
#         __init__.py
#         admin.py
#         apps.py
#         migrations/
#             __init__.py
#         models.py
#         tests.py
#         views.py
#         urls.py

# about urls:

# creart response on polls/views.py like
from  django.http import HttpResponse
def index(request):
    return HttpResponse("hello")
# create urls on polls/urls.py like
from django.urls import path 
from . import views
urlpatterns = [
    path('',views.index,name='index'),
]
# add urls on mysite/urls.py like
# ...
from django.urls import path,include
urlpatterns = [
    path('polls/',include('polls.urls'))
]


# url in html:
# use the "name" in urls.py
# such as 
# app_name = 'polls'
# path('<int:question_id>/',views.detail,name='detail')
# then in html:
# <a href="{% url 'polls:detail' question.id %}">