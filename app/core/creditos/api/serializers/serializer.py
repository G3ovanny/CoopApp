from rest_framework import serializers
from app.core.creditos.models import FormaPago, TipoGarantia, TipoSolicitud, TipoSegmentacion, SolicitudCredito, DetalleSolicitud

class FormaPagoSerializer(serializers.ModelSerializer):
    class Meta:
        model = FormaPago
        fields = '__all__'

class TipoGarantiaSerializer(serializers.ModelSerializer):
    class Meta:
        model = TipoGarantia
        fields = '__all__'

class TipoSolicitudSerializer(serializers.ModelSerializer):
    class Meta:
        model = TipoSolicitud
        fields = '__all__'

class TipoSegmentacionSerializer(serializers.ModelSerializer):
    class Meta:
        model = TipoSegmentacion
        fields = '__all__'

class SolicitudSerializer(serializers.ModelSerializer):
    class Meta:
        model = SolicitudCredito
        fields = '__all__'

class DetalleSolicitudSerializer(serializers.ModelSerializer):
    class Meta:
        model = DetalleSolicitud
        fields = '__all__'