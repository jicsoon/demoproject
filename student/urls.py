from django.urls import path,include 
from . import views

app_name='student'

urlpatterns = [
    path('', views.register,name='register'),
    path('display', views.display,name='display'),
    path('update/<int:id>', views.update,name='update'),
    path('delete/<int:id>', views.delete,name='delete'),
]


