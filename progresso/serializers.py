from rest_framework import serializers
from .models import Progress

class ProgressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Progress
        fields = ['id', 'student', 'content', 'completed', 'completed_at']
        read_only_fields = ['completed_at']