from django.contrib.auth.models import User
from django.db import models

class Event(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    date = models.DateField()
    time = models.TimeField()
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)

    # New category field
    CATEGORY_CHOICES = [
        ('workshop', 'Workshop'),
        ('meeting', 'Meeting'),
        ('webinar', 'Webinar'),
        ('conference', 'Conference'),
    ]
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES, default='meeting')

    def __str__(self):
        return self.title
