from django.db import models
from courses.models import Module

class Content(models.Model):
    CONTENT_TYPES = [
        ('video', 'Vídeo'),
        ('pdf', 'PDF'),
        ('link', 'Link'),
        ('text', 'Texto'),
    ]

    module = models.ForeignKey(Module, related_name='contents', on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    content_type = models.CharField(max_length=10, choices=CONTENT_TYPES)
    text = models.TextField(blank=True, null=True)
    url = models.URLField(blank=True, null=True)
    file = models.FileField(upload_to='content_files/', blank=True, null=True)

    def __str__(self):
        return self.title