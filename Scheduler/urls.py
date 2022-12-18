from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('createCourse/', views.createCourse_view, name='createCourse'),
    path('createUser/', views.createUser_view, name='createUser'),
]
