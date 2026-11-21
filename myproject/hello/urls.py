from django.urls import path
from . import views

urlpatterns = [
    path ('', views.hello, name='hello'),
    path ('add/', views.add, name='add'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('register/', views.register, name='register'),
    path('delete/<int:activity_id>/', views.delete_activity, name='delete_activity'),
    path('edit/<int:activity_id>/', views.edit_activity, name='edit_activity'),
]