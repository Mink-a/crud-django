from . import views
from django.urls import path

urlpatterns = [
    path('', views.allTodos, name='all-todos'),
    path('add/', views.addTodo, name='add-todo'),
    path('delete/<int:id>', views.deleteTodo, name='delete-todo'),
    path('update/<int:id>', views.updateTodo, name='update-todo'),
]
