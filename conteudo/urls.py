from django.urls import path
from .views import ContentListView, ContentByModuleView

urlpatterns = [
    path('', ContentListView.as_view(), name='content-list'),
    path('module/<int:module_id>/', ContentByModuleView.as_view(), name='content-by-module'),
]