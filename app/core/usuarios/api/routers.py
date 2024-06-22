from rest_framework.routers import DefaultRouter
from app.core.usuarios.api.views.usuarios_views import UsuarioViewSet
from app.core.usuarios.api.views.grupos_views import GruposViewSet
from app.core.usuarios.api.views.reset_password_views import ResetPasswordViews

router = DefaultRouter()

router.register(r'usuario', UsuarioViewSet, basename='usuario')
router.register(r'grupos', GruposViewSet, basename='grupos')
urlpatterns = router.urls