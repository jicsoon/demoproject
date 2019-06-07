from django.urls import path,include 
from . import views




urlpatterns = [
    path('', views.home,name='home'),
    path('add',views.addTodo,name='add'),
    path('complete/<todo_id>',views.completedTodo,name='complete'),
    path('deletecomplete',views.deleteCompleted,name='deletecomplete'),
    path('deleteall',views.deleteAll,name='deleteall'),
   
]