from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=100)
    course = models.CharField(max_length=100)
    progress_percent = models.IntegerField(default=0)
    study_time_hours = models.DecimalField(max_digits=5, decimal_places=1)
    last_access = models.CharField(max_length=50)

    def __str__(self):
        return self.name