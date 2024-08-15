from rest_framework.routers import DefaultRouter
from app.core.creditos.api.views.formasPago_views import FormaPagoViewSet
from app.core.creditos.api.views.tipoGarantias_views import TipoGarantiaViewSet
from app.core.creditos.api.views.tipoSolicitud_views import TipoSolicitudViewSet
from app.core.creditos.api.views.tipoSegmentacion_views import TipoSegmentacionViewSet
from app.core.creditos.api.views.detalleSolicitud_views import DetalleSolicitudViewSet
from app.core.creditos.api.views.solicitudCredito_views import SolicitudViewSet
router = DefaultRouter()

router.register(r'formas-pagos', FormaPagoViewSet, basename='forma_pago')
router.register(r'tipos-garantia', TipoGarantiaViewSet, basename='tipos_garantia')
router.register(r'tipos-solicitud', TipoSolicitudViewSet, basename='tipos_solicitud')
router.register(r'tipos-segmentacion', TipoSegmentacionViewSet, basename='tipos_segmentacion')
router.register(r'solicitud', SolicitudViewSet, basename='solicitud')
router.register(r'detalle-solicitud', DetalleSolicitudViewSet, basename='detalle_solicitud')

urlpatterns = router.urls