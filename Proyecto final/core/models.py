from tabnanny import verbose
from unicodedata import category
from django.db import models
from django.utils.html import format_html

class Empleados(models.Model):
    nombre = models.CharField(max_length=40, verbose_name='Nombre')
    apellido = models.CharField(max_length=40,  verbose_name='Apellido')
    foto = models.ImageField(upload_to='media', null=True, blank=True)
    Cargo = models.CharField(max_length=40, verbose_name='Cargo')
    Tipo_Contrato = models.CharField(max_length=40, verbose_name='Tipo Contrato')
    hora = models.DurationField(verbose_name='Hora de ingreso')
    hora2 = models.DurationField(verbose_name='Hora de salida')
    
    def show_image(self):
        return format_html('<img src={} width="100" />', self.foto.url)

    def __str__(self):
        return self.nombre
    
    
    class Meta:
        verbose_name = 'Empleado'
        verbose_name_plural = 'Empleados'
        db_table = 'empleado'
        ordering = ['id']
    
class Inventario(models.Model):
    categoria = models.CharField(max_length=100, verbose_name='Categoría')
    descripcion = models.TextField(verbose_name='Descripción')
    fecha_ingreso = models.DateTimeField(verbose_name='Fecha de ingreso')
    fecha_salida = models.DateTimeField(verbose_name='Fecha de salida')
    empleados = models.ForeignKey(Empleados, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.categoria
    
    class Meta:
        verbose_name = 'Inventario'
        verbose_name_plural = 'Inventarios'
        db_table = 'Inventario'
        ordering = ['id']
    
class Utilidades(models.Model):
    codigo = models.CharField(max_length=100, verbose_name='Código')
    nombre = models.CharField(max_length=50, verbose_name='Nombre')
    marca = models.CharField(max_length=50, verbose_name='Marca')
    imagen_producto = models.ImageField(upload_to='media', null=True, blank=True)
    precio = models.IntegerField(verbose_name='Precio')
    cantidad = models.DecimalField(max_digits=4, decimal_places=0, verbose_name='Cantidad')
    categoria = models.ForeignKey(Inventario, on_delete=models.CASCADE)
    disponible = models.BooleanField(verbose_name='¿Producto Disponible?')
    
    def show_image(self):
        return format_html('<img src={} width="100" />', self.imagen_producto.url)
    
    def __str__(self):
        return self.nombre
    
    class Meta:
        verbose_name = 'Utilidad'
        verbose_name_plural = 'Utilidades'
        db_table = 'Utilidades'
        ordering = ['id']
        
class Proyectos(models.Model):
    nombre_proyecto = models.CharField(max_length=50, verbose_name='Nombre Proyecto')
    fecha_inicio = models.DateField(verbose_name='Fecha de Inicio')
    fecha_final = models.DateField(verbose_name='Fecha Final')
    ciudad = models.CharField(max_length=30, verbose_name='Ciudad')
    descripcion = models.TextField(verbose_name='Descripción')
    observaciones = models.TextField(verbose_name='Observaciones')
    empleados = models.ManyToManyField(Empleados)
    
    def __str__(self):
        return self.nombre_proyecto
    
    class Meta:
        verbose_name = 'Proyecto'
        verbose_name_plural = 'Proyectos'
        db_table = 'Proyecto'
        ordering = ['id']

class Clientes(models.Model):
    primer_nombre = models.CharField(max_length=50, verbose_name='Nombre')
    primer_apellido = models.CharField(max_length=50, verbose_name='Apellido')
    direccion = models.CharField(max_length=60, verbose_name='Dirección')
    telefono = models.IntegerField(verbose_name='Teléfono')
    email = models.CharField(max_length=90, verbose_name='Correo Electrónico')
    tipo_servicio = models.CharField(max_length=150, verbose_name='Tipo de Servicio')
    observaciones = models.TextField(verbose_name='Observaciones')
    
    def __str__(self):
        return self.primer_nombre
    
    class Meta:
        verbose_name = 'Cliente'
        verbose_name_plural = 'Clientes'
        db_table = 'Cliente'
        ordering = ['id']

class Producto(models.Model):
    nombre = models.CharField(max_length=64)
    categoria = models.CharField(max_length=32)
    precio = models.IntegerField()
    foto_producto = models.ImageField(upload_to='media', null=True, blank=True)
    
    def show_image(self):
        return format_html('<img src={} width="100" />', self.foto_producto.url)
    
    def __str__(self):
        return f'{self.nombre} -> {self.precio}'