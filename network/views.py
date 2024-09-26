from rest_framework import viewsets, permissions
from .models import NetworkNode
from .serializers import NetworkNodeSerializer, NetworkNodeListSerializer


class NetworkNodeViewSet(viewsets.ModelViewSet):
    """CRUD представление для Узла сети."""
    queryset = NetworkNode.objects.all()
    permission_classes = [permissions.IsAuthenticated]  # Доступ для активных сотрудников

    def get_serializer_class(self):
        if self.action == 'list':
            return NetworkNodeListSerializer
        return NetworkNodeSerializer
