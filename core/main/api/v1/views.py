from rest_framework.viewsets import ModelViewSet
from .serializers import ToDoSerializer
from main.models import ToDoList
from rest_framework.permissions import IsAuthenticated
from rest_framework.filters import SearchFilter,OrderingFilter

class ListModelViewSet(ModelViewSet):
    serializer_class = ToDoSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [SearchFilter,OrderingFilter]
    search_fields = ['content']
    ordering_fields = ['created']
    def get_queryset(self):
        return ToDoList.objects.filter(author = self.request.user)
        
        

