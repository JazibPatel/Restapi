from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.Overview, name='overview'),
    path('employees/', views.EmployList, name='employees.index'),
    path('employdetail/<str:id>/', views.EmployDetail, name='employdetail'),
    path('employcreate/', views.EmployCreate, name='employcreate'),
    path('employupdate/<str:id>/', views.EmployUpdate, name='employupdate'),
    path('employdelete/<str:id>/', views.EmployDelete, name='employdelete'),
]