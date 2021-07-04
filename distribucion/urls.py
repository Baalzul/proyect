from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),

    path("busqueda_en_inventario/", views.busqueda_en_inventario, name='busqueda en inventario'),
    path("reporte_de_inventario/", views.reporte_de_inventario, name='reporte de inventario'),
    path("busqueda_de_clientes/", views.busqueda_de_clientes, name='busqueda de clientes'),
    path("reporte_de_clientes/", views.reporte_de_clientes, name='reporte de clientes'),
    path("orden_de_compra/", views.orden_de_compra, name='orden de compra'),
    path("reporte_ordenes_de_compra/", views.reporte_ordenes_de_compra, name='reporte ordenes de compra'),
    path("productos/", views.productos, name='productos'),
]