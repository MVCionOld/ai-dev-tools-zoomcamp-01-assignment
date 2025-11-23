from django.urls import path
from . import views

app_name = 'todos'

urlpatterns = [
    path('', views.index, name='index'),
    path('api/todos/', views.todo_list, name='todo_list'),
    path('api/todos/create/', views.todo_create, name='todo_create'),
    path('api/todos/<int:todo_id>/update/', views.todo_update, name='todo_update'),
    path('api/todos/<int:todo_id>/delete/', views.todo_delete, name='todo_delete'),
]
