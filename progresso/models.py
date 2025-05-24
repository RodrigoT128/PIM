from django.db import models
from users.models import Student
from content.models import Content

class Progress(models.Model):
    student = models.ForeignKey(Student, related_name='progress', on_delete=models.CASCADE)
    content = models.ForeignKey(Content, related_name='progress_entries', on_delete=models.CASCADE)
    completed = models.BooleanField(default=False)
    completed_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('student', 'content')

    def __str__(self):
        return f"{self.student.username} - {self.content.title} - {'✔' if self.completed else '❌'}"