from rest_framework import viewsets, status
from rest_framework.response import Response 
from ...models import FormaPago
from ..serializers.serializer import *

class FormaPagoViewSet(viewsets.ModelViewSet):
    serializer_class = FormaPagoSerializer
    
    def get_queryset(self, pk=None):
        if pk is None:
            return self.get_serializer().Meta.model.objects.filter(state = True)
        return self.get_serializer().Meta.model.objects.filter(id=pk, state = True).first()
    
    def create(self, request):
        pagos_serializer = self.serializer_class(data=request.data)
        if pagos_serializer.is_valid():
            pagos_serializer.save()
            return Response({'message':'La forma de pago se a creado correctamente'}, status=status.HTTP_201_CREATED)
        return Response(pagos_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def update(self, request, pk=None):
        if self.get_queryset(pk):
            pagos_serializer = self.serializer_class(self.get_queryset(pk), data=request.data)
            if pagos_serializer.is_valid():
                # pagos_serializer.save()
                pagos_serializer.update(self.get_queryset(pk), pagos_serializer.validated_data)
                return Response({'message':'La forma de pago se actualizó correctamente'}, status=status.HTTP_200_OK)
            return Response(pagos_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk=None):
        pago = self.get_queryset().filter(id = pk).first()
        print(pago)
        if pago :
            pago.state = False
            pago.save()
            return Response({'message':'La forma de pago se ha eliminado correctamente'}, status=status.HTTP_200_OK)
        return Response({'error':'No existe la forma de pago con esos datos'}, status=status.HTTP_400_BAD_REQUEST)