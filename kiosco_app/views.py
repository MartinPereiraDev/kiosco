from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import Producto, CarritoCompra, Venta
from rest_framework.permissions import AllowAny
from rest_framework import generics

from .serializers import ProductoSerializer, User, CarritoCompraSerializer, VentaSerializer, RegistroUsuarioSerializer


class ProductoViewSet(viewsets.ModelViewSet):
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer

class CarritoCompraViewSet(viewsets.ModelViewSet):
    queryset = CarritoCompra.objects.all()
    serializer_class = CarritoCompraSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return CarritoCompra.objects.filter(usuario=self.request.user)

class VentaViewSet(viewsets.ModelViewSet):
    queryset = Venta.objects.all()
    serializer_class = VentaSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Venta.objects.filter(usuario=self.request.user)
    

#class register users    
class RegistroUsuarioView(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = RegistroUsuarioSerializer