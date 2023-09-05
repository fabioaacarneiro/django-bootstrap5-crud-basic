from django.contrib import admin
from django.urls import path
from app_cadastro_usuarios import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('users/', views.users, name='users_list'),
    path('users/<int:id>/', views.user_update, name='user_update'),
    path('users_delete/<int:id>/', views.user_delete, name='user_delete'),
]
