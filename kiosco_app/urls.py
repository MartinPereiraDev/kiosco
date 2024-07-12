from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ProductoViewSet, CarritoCompraViewSet, VentaViewSet
from .views import RegistroUsuarioView

router = DefaultRouter()
router.register(r'productos', ProductoViewSet)
router.register(r'carrito', CarritoCompraViewSet)
router.register(r'ventas', VentaViewSet)


urlpatterns = [
    path('', include(router.urls)),
    path('registro/', RegistroUsuarioView.as_view(), name='auth_register'),
]