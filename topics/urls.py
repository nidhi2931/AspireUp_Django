from django.urls import path
from .views import *

urlpatterns=[
    path('get/',get_topics,name='get_topics'),
    path('create/',create_topics,name='create_topics'),
]