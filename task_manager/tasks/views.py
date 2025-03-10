from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from .models import Task
from .forms import TaskForm

# Display the list of all tasks
def task_list(request):
    tasks = Task.objects.all()  # Fetch all tasks from the database
    return render(request, 'tasks/task_list.html', {'tasks': tasks})

# Create a new task
def task_create(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)  # Populate the form with submitted data
        if form.is_valid():  # Validate form data
            form.save()  # Save task to database
            messages.success(request, 'Task created successfully!')  # Show success message
            return redirect('task_list')  # Redirect to task list page
    else:
        form = TaskForm()  # Create an empty form for GET request
    return render(request, 'tasks/task_form.html', {'form': form})

# Edit an existing task
def task_update(request, id):
    task = get_object_or_404(Task, id=id)  # Fetch task by ID or return 404 if not found
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)  # Populate form with existing data
        if form.is_valid():  # Validate form data
            form.save()  # Save updated task details
            messages.success(request, 'Task updated successfully!')  # Show success message
            return redirect('task_list')  # Redirect to task list page
    else:
        form = TaskForm(instance=task)  # Pre-fill form with task data for GET request
    return render(request, 'tasks/task_form.html', {'form': form})

# Delete a task
def task_delete(request, id):
    task = get_object_or_404(Task, id=id)  # Fetch task by ID or return 404 if not found
    if request.method == 'POST':
        task.delete()  # Remove task from database
        messages.success(request, 'Task deleted successfully!')  # Show success message
        return redirect('task_list')  # Redirect to task list page
    return render(request, 'tasks/task_confirm_delete.html', {'task': task})

# Mark a task as completed
def task_complete(request, id):
    task = get_object_or_404(Task, id=id)  # Fetch task by ID or return 404 if not found
    task.status = 'Completed'  # Update task status
    task.save()  # Save changes to database
    messages.success(request, 'Task marked as completed!')  # Show success message
    return redirect('task_list')  # Redirect to task list page
