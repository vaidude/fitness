from .import views
from django.urls import path

urlpatterns=[
    path('',views.index,name='index'),
    path('index/',views.index,name='index'),
    path('home/',views.home,name='home'),
    path('register/',views.register,name='register'),
    path('login/',views.login,name='login'),
    path('profile/',views.profile,name='profile'),
    path('editprofile/',views.editprofile,name='editprofile'),
    path('logout/',views.logout,name='logout'),
    path('listvideo/', views.video_list, name='listvideo'),
    path('addvideo/', views.video_add, name='addvideo'),
    path('fitness_tracker/', views.fitness_tracker, name='fitness_tracker'),
]
