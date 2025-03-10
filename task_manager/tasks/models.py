from django.db import models  
from django.utils import timezone  

#Incharge of the structure of a "Task" in the database
class Task(models.Model):
    # Predefined choices for task status
    STATUS_CHOICES = [
        ('Pending', 'Pending'),  # Task is not yet completed
        ('Completed', 'Completed'),  # Task has been successfully completed
        ('Overdue', 'Overdue'),  # Task was not completed on time
    ]

    title = models.CharField(max_length=100)  # Task title
    description = models.TextField(blank=True, null=True)  # Optional task description
    due_date = models.DateField()  # Task deadline
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Pending')  # Task status

    def __str__(self):
        return self.title  # Display task title when printed

    def save(self):
        """Automatically marks tasks as 'Overdue' if the due date has passed before saving."""
        if self.due_date < timezone.now().date():
            self.status = 'Overdue'
        super().save()  # Save task in the database
