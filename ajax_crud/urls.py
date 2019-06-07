from django.urls import path,include 
from . import views

app_name='ajax_crud'

urlpatterns = [
    path('', views.register,name='register'),
    path('visitor/',views.visitor_list,name='visitor_list'),
    path('create/',views.createVisitor,name='createVisitor'),

] 