from django.urls import path
from django.conf.urls import url
from . import views

urlpatterns = [
    # path('', views.help, name='help'),
    url(r'^$', views.help, name='help'),
]
