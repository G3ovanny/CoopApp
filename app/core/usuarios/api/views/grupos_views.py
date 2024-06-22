from rest_framework import viewsets, status, mixins
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.models import Group
from app.core.usuarios.api.serializers.grupos_serializers import UserGroupSerializer

class GruposViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    serializer_class = UserGroupSerializer
    queryset = Group.objects.all()
    permission_classes = [IsAuthenticated]

    def list(self, request, *args, **kwargs):
        grupos = self.queryset
        if not grupos.exists():
            return Response({"detail": "No groups found"}, status=status.HTTP_404_NOT_FOUND)
        
        grupo_serializer = self.serializer_class(grupos, many=True)
        return Response(grupo_serializer.data, status=status.HTTP_200_OK)