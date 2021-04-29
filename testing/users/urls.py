from django.contrib import admin
from django.urls import path
from users import views

urlpatterns = [
    path('register/', views.register),
    path('login/', views.login),
    path('user-list', views.userList),
    path('edit_view', views.userEditView),
    path('update_user', views.updateUser)
]