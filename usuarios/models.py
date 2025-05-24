from django.contrib.auth.models import AbstractUser
from django.db import models

class Student(AbstractUser):
    enrollment = models.CharField(max_length=8, unique=True)

    def __str__(self):
        return f"{self.username} ({self.enrollment})"