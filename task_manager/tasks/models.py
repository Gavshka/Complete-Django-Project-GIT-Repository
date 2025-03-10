from django.db import models  
from django.utils import timezone  

class Task(models.Model):
    # Define possible status choices for a task
    STATUS_CHOICES = [
        ('Pending', 'Pending'),  # Task is upcoming
        ('Due Today', 'Due Today'),  # Task is due today
        ('Overdue', 'Overdue'),  # Task is past its due date
        ('Completed', 'Completed'),  # Task has been marked as completed
    ]

    title = models.CharField(max_length=100)  # The name of the task (required)
    description = models.TextField(blank=True, null=True)  # Optional details about the task
    due_date = models.DateField()  # The deadline for completing the task
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Pending')  # Task status with a default value

    def __str__(self):
        # Defines how the task appears when printed or displayed in the admin panel.
        return self.title  

    def save(self):
        # Automatically updates the task status before saving it to the database
        today = timezone.now().date()  # Get today's date

        # If the task is not already marked as "Completed", update its status
        if self.status != 'Completed':  
            if self.due_date < today:  # If the due date has passed, mark it as "Overdue"
                self.status = 'Overdue'
            elif self.due_date == today:  # If it's due today, mark it as "Due Today"
                self.status = 'Due Today'
            else:  # If the due date is in the future, keep it "Pending"
                self.status = 'Pending'

        super().save()  # Call Django's default save method to store changes
