from django.urls import path
from . import views


app_name = 'contact'


urlpatterns = [
    path('', views.home, name='home'),
    path('users/', views.users, name='users_list'),
    path('users/<int:id>/', views.user_update, name='user_update'),
    path('users_delete/<int:id>/', views.user_delete, name='user_delete'),
]