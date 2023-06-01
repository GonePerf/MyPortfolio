from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.loginPage, name="login"),
    path('logout/', views.logoutUser, name="logout"),

    path('', views.home, name='home'),
    path('tools', views.tools, name='tools'),
    path('projects', views.projects, name='projects'),
    # path('tool/<str:pk>', views.tool, name='tool'),
    # path('profile/<str:pk>', views.userProfile, name='user-profile'),
    # path('create-tool/', views.createTool, name="create-tool"),
    # path('update-tool/<str:pk>', views.updateTool, name="update-tool"),
    # path('delete-tool/<str:pk>', views.deleteTool, name="delete-tool"),
    # path('delete-message/<str:pk>', views.deleteMessage, name="delete-message"),
]
