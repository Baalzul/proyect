from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Producto, Cliente, Orden_de_compra


def index(request):
    return render(request, 'distribucion/index.html')

#----------------------------------------------
def busqueda_en_inventario(request):
    productos = Producto.objects.all
    productos = {'lista_productos': productos}
    return render(request, 'distribucion/busqueda en inventario.html',productos)

def reporte_de_inventario(request):
    productos = Producto.objects.all
    data = {
        'data' : productos
    }
    return render(request, 'distribucion/reporte de inventario.html',data)
#----------------------------------------------
def busqueda_de_clientes(request):
    clientes = Cliente.objects.all
    clientes = {'lista_productos': clientes}
    return render(request, 'distribucion/busqueda de cliente.html',clientes)

def reporte_de_clientes(request):
    clientes = Cliente.objects.all
    clientes = {'lista_productos': clientes}
    return render(request, 'distribucion/reporte de clientes.html',clientes)
#-----------------------------------------
def orden_de_compra(request):
    return render(request, 'distribucion/orden de compra.html')

def reporte_ordenes_de_compra(request):
    orden = Orden_de_compra.objects.all
    orden = {'lista_orden': orden}
    return render(request, 'distribucion/reporte ordenes de compra.html', orden)
#---------------------------------------------
def productos(request):
    return render(request, 'distribucion/productos.html')