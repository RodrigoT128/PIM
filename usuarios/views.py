from rest_framework import generics
from .models import Student
from .serializers import StudentSerializer

class RegisterView(generics.CreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer