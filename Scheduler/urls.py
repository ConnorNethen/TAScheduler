from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('users/', views.all_users, name='all_users'),
    path('users/new/', views.new_user, name='new_user'),
    path('courses/', views.all_courses, name='all_courses'),
    path('courses/new/', views.new_course, name='new_course'),
    path('courses/<str:course_number>/', views.course, name='course'),
    path('courses/<str:course_number>/new-section/', views.new_section, name='new_section'),
]