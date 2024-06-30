from django.contrib import admin
from django.urls import path, include, re_path
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from app.core.usuarios.views import Login, Logout
from app.core.usuarios.views import ResetPass

schema_view = get_schema_view(
   openapi.Info(
      title="Cooperativa API",
      default_version='v0.1',
      description="Documentación guia para la utilización del api de la cooperativa",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="fronteratech@gmail.com"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('swagger<format>/', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    path('admin/', admin.site.urls),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    #rutas api
    path('loging/', Login.as_view(), name='login'),   
    path('logout/', Logout.as_view(), name='logout'),
    path('reset_pass/', ResetPass.as_view(), name='reset_password' ),
    path('usuarios/', include('app.core.usuarios.api.routers')),
]
