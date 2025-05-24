from rest_framework import generics, permissions
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from courses.models import Course
from content.models import Content
from .models import Progress
from .serializers import ProgressSerializer

class ProgressListCreateView(generics.ListCreateAPIView):
    serializer_class = ProgressSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Progress.objects.filter(student=self.request.user)

    def perform_create(self, serializer):
        serializer.save(student=self.request.user)

class CourseProgressView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, course_id):
        user = request.user

        # Obter todos os conteúdos do curso
        try:
            course = Course.objects.get(id=course_id)
        except Course.DoesNotExist:
            return Response({"detail": "Curso não encontrado."}, status=404)

        all_contents = Content.objects.filter(module__course=course)
        total = all_contents.count()

        # Filtrar progresso do usuário nos conteúdos desse curso
        completed_count = Progress.objects.filter(
            student=user,
            content__in=all_contents,
            completed=True
        ).count()

        percent = (completed_count / total) * 100 if total > 0 else 0

        return Response({
            "course": course.title,
            "total_contents": total,
            "completed_contents": completed_count,
            "completion_percent": round(percent, 2)
        })