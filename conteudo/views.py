from rest_framework import generics
from .models import Content
from .serializers import ContentSerializer

class ContentListView(generics.ListAPIView):
    queryset = Content.objects.all()
    serializer_class = ContentSerializer

class ContentByModuleView(generics.ListAPIView):
    serializer_class = ContentSerializer

    def get_queryset(self):
        module_id = self.kwargs['module_id']
        return Content.objects.filter(module_id=module_id)