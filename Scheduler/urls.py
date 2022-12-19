from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.login_view, name='login'),
    path('allCourses/', views.allCourses_view, name='All Courses'),
    path('allUsers/', views.allUsers_view, name='All Users'),
    path('userPage/', views.user_view, name='myUserPage'),
    path('user/<int:pantherID>/', views.user_view, name='userPage'),
    path('logout/', views.logout_view, name='logout'),
    path('createSection/', views.createSection_view, name='createSection'),
]
