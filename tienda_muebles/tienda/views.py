from django.shortcuts import render, get_object_or_404
from .models import Producto

def lista_productos(request):
    productos = Producto.objects.filter(disponible=True)
    return render(request, 'tienda/lista_productos.html', {'productos': productos})

def detalle_producto(request, pk):
    producto = get_object_or_404(Producto, pk=pk, disponible=True)
    return render(request, 'tienda/detalle_producto.html', {'producto': producto})
