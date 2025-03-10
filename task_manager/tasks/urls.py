from django.urls import path  
from . import views  

# Incharge of defining URL patterns for task-related views.
urlpatterns = [
    path('', views.task_list, name='task_list'),  # Displays a list of all tasks
    path('create/', views.task_create, name='task_create'),  # Page for creating a new task
    path('<int:id>/edit/', views.task_update, name='task_update'),  # Edit an existing task
    path('<int:id>/delete/', views.task_delete, name='task_delete'),  # Delete a task
    path('<int:id>/complete/', views.task_complete, name='task_complete'),  # Mark task as completed
]
