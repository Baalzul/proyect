from django.contrib import admin

from .models import Producto,Inventario,Detalle_inventario,Orden_de_compra,Cliente,Orden_cliente

admin.site.register(Producto)
admin.site.register(Inventario)
admin.site.register(Detalle_inventario)
admin.site.register(Orden_de_compra)
admin.site.register(Cliente)
admin.site.register(Orden_cliente)
