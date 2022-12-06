from django.urls import path

from . import views

urlpatterns = [
    path('', views.Index.as_view(), name='index'),
    path('login/', views.Login.as_view(), name='login'),
    # path('logout/', views.logout, name='logout'),
    path('users/', views.AllUsers.as_view(), name='all_users'),
    path('users/new/', views.CreateUser.as_view(), name='create_user'),
    # path('courses/', views.all_courses, name='all_courses'),
    path('courses/new/', views.CreateCourse.as_view(), name='create_course'),
    # path('courses/<str:course_number>/', views.course, name='course'),
    path('courses/<str:course_number>/new-section/', views.new_section, name='new_section'),
    path('users/', views.DeleteUser.as_view(), name='delete_user'),
    path('users/<str:user_pid>/', views.UserPage, name='user_page'),
]