from django.urls import path
from django.conf.urls import url
from . import views

# SET THE NAMESPACE!
app_name = 'basic_app'

urlpatterns = [
    path('relative/', views.relative, name='relative'),
    path('other/', views.other, name='other'),
]

#
# urlpatterns = [
#     url(r'^relative/$', views.relative, name='relative'),
#     url(r'^other/$', views.other, name='other'),
# ]
