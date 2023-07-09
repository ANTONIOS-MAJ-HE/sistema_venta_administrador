from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

# Crea un enrutador para las vistas basadas en clases
router = DefaultRouter()
router.register(r'usuarios', views.UsuarioViewSet)
router.register(r'roles', views.RolViewSet)
# Agrega los otros modelos al enrutador
router.register(r'usuario-roles', views.UsuarioRolViewSet)
router.register(r'productos', views.ProductoViewSet)
router.register(r'comentarios', views.ComentarioViewSet)

# Agrega las rutas generadas por el enrutador a las rutas principales
urlpatterns = [
    path('', include(router.urls)),
]
