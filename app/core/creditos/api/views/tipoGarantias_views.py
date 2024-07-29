from rest_framework import viewsets, status
from rest_framework.response import Response 
from ..serializers.serializer import *

class TipoGarantiaViewSet(viewsets.ModelViewSet):
    serializer_class = TipoGarantiaSerializer
    
    def get_queryset(self, pk=None):
        if pk is None:
            return self.get_serializer().Meta.model.objects.filter(state = True)
        return self.get_serializer().Meta.model.objects.filter(id=pk, state = True).first()
    
    def create(self, request):
        garantia_serializer= self.get_serializer_class(data=request.data)
        if garantia_serializer.is_valid():
            garantia_serializer.save()
            return Response({'message','El tipo de garantia se a creado correctamente'}, status=status.HTTP_201_CREATED)
        return Response(garantia_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def update(self, request, pk=None):
        if self.get_queryset(pk):
            garantia_serializer= self.get_serializer_class(self.get_queryset(pk), data = request.data)
            if garantia_serializer.is_valid():
                # garantia_serializer.save()
                garantia_serializer.update(self.get_queryset(pk), garantia_serializer.validated_data)
                return Response({'message','El tipo de garantia se actualizó correctamente'}, status=status.HTTP_200_OK)
            return Response(garantia_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def destroy(self, request, pk=None):
        pago = self.get_queryset().filter(id = pk).first()
        if pago :
            pago.state = False
            pago.save()
            return Response({'message','El tipo de garantia se ha eliminado correctamente'}, status=status.HTTP_200_OK)
        return Response({'error', 'No existe el tipo de garantia con esos datos'}, status=status.HTTP_400_BAD_REQUEST)