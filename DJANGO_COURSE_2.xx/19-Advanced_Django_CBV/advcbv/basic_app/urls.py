from django.urls import path
from . import views

app_name = 'basic_app'

urlpatterns = [
    path('schools/', views.SchoolListView.as_view(), name='schools_list'),
    path('students/', views.StudentListView.as_view(), name='students_list'),
    path('schools/<int:pk>/', views.SchoolDetailView.as_view(), name='school_detail'),
    path('students/<int:pk>/', views.StudentDetailView.as_view(), name='student_detail'),
    # url(r'^(?P<pk>[-\w]+)/$', views.SchoolDetailView.as_view(), name='detail'),
    path('create_student/', views.StudentCreateView.as_view(), name='create_student'),
    path('create_school/', views.SchoolCreateView.as_view(), name='create_school'),
    path('update_school/<int:pk>/', views.SchoolUpdateView.as_view(), name='update_school'),
    path('update_student/<int:pk>/', views.StudentUpdateView.as_view(), name='update_student'),
    path('delete_school/<int:pk>/', views.SchoolDeleteView.as_view(), name='delete_school'),
    path('delete_student/<int:pk>/', views.StudentDeleteView.as_view(), name='delete_student')
]
