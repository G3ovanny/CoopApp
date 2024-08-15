from rest_framework import viewsets, status
from rest_framework.response import Response 
from ..serializers.serializer import *

class SolicitudViewSet(viewsets.ModelViewSet):
    serializer_class = SolicitudSerializer
    
    def get_queryset(self, pk=None):
        if pk is None:
            return self.get_serializer().Meta.model.objects.filter(state = True)
        return self.get_serializer().Meta.model.objects.filter(id=pk, state = True).first()
    
    def create(self, request):
        solicitud_serializer= self.serializer_class(data=request.data)
        if solicitud_serializer.is_valid():
            solicitud_serializer.save()
            return Response({'message','La solicitud se a creado correctamente'}, status=status.HTTP_201_CREATED)
        return Response(solicitud_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def update(self, request, pk=None):
        if self.get_queryset(pk):
            solicitud_serializer= self.serializer_class(self.get_queryset(pk), data = request.data)
            if solicitud_serializer.is_valid():
                # solicitud_serializer.save()
                solicitud_serializer.update(self.get_queryset(pk), solicitud_serializer.validated_data)
                return Response({'message','La solicitud se actualizó correctamente'}, status=status.HTTP_200_OK)
            return Response(solicitud_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def destroy(self, request, pk=None):
        pago = self.get_queryset().filter(id = pk).first()
        if pago :
            pago.state = False
            pago.save()
            return Response({'message','La solicitud se ha eliminado correctamente'}, status=status.HTTP_200_OK)
        return Response({'error', 'No existe la solicitud con esos datos'}, status=status.HTTP_400_BAD_REQUEST)