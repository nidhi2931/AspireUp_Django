from django.urls import path
from .views import *
from django.conf import settings
from django.conf.urls.static import static


urlpatterns=[
    path('get/',get_adddocs,name='get_adddocs'),
    path('create/',create_adddocs,name='create_adddocs'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)