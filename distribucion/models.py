from django.db import models

class Producto(models.Model):
    nombre = models.CharField(max_length=200)
    tipo = models.CharField(max_length=200)
    codigo = models.CharField(max_length=200)
    marca = models.CharField(max_length=200)
    descripcion = models.CharField(max_length=200)

    def __str__(self):
        return self.codigo

class Inventario(models.Model):
    nombre = models.CharField(max_length=200)
    codigo = models.CharField(max_length=200)

    def __str__(self):
        return self.codigo

class Detalle_inventario(models.Model):
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    inventario = models.ForeignKey(Inventario, on_delete=models.CASCADE)
    codigo = models.CharField(max_length=200)
    cantidad = models.CharField(max_length=200)
    fecha_de_salida = models.DateTimeField('fecha de entrada')

    def __str__(self):
        return self.codigo

class Orden_de_compra(models.Model):
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    detalle_inventario = models.ForeignKey(Detalle_inventario, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=200)
    codigo = models.CharField(max_length=200)
    fecha_de_salida = models.DateTimeField('fecha de salida')

    def __str__(self):
        return self.codigo

class Cliente(models.Model):
    codigo = models.CharField(max_length=200)
    nombre = models.CharField(max_length=200)
    pais = models.CharField(max_length=200)
    region = models.CharField(max_length=200)
    cuidad = models.CharField(max_length=200)
    comuna = models.CharField(max_length=200)
    direccion = models.CharField(max_length=200)
    email = models.CharField(max_length=200)

    def __str__(self):
        return self.codigo

class Orden_cliente(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    orden_compra = models.ForeignKey(Orden_de_compra, on_delete=models.CASCADE) 
    codigo = models.CharField(max_length=200)
    fecha_de_pedido = models.DateTimeField('fecha de pedido')
    cantidad = models.IntegerField(default=0)
    codigo = models.CharField(max_length=200)

    def __str__(self):
        return self.codigo

