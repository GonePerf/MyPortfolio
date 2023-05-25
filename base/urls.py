from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.loginPage, name="login"),
    path('register/', views.registerUser, name="register"),
    path('logout/', views.logoutUser, name="logout"),

    path('', views.home, name='home'),
    path('technologies', views.technologies, name='technologies'),
    path('projects', views.projects, name='projects'),

    path('skill/<str:pk>', views.skill, name='skill'),
    path('profile/<str:pk>', views.userProfile, name='user-profile'),
    path('create-skill/', views.createSkill, name="create-skill"),
    path('update-skill/<str:pk>', views.updateSkill, name="update-skill"),
    path('delete-skill/<str:pk>', views.deleteSkill, name="delete-skill"),
    path('delete-message/<str:pk>', views.deleteMessage, name="delete-message")
]
