from django.urls import path
from .views import *

urlpatterns=[
    path('add/',AddSubjectView.as_view(),name='add_subject'),
    path('get/',GetSubjectView.as_view(),name='get_subjects'),
]