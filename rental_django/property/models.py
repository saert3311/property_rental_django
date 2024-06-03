from rental_django.settings import MEDIA_URL, STATIC_URL
from django.db import models
from users.models import Comuna
from django.contrib.auth.models import User
# Create your models here.

class Property(models.Model):
    TYPE_CHOICES = (
        ( 0, 'Casa'),
        ( 1, 'Departamento'),
        ( 2, 'Parcela'),
        ( 3, 'Local'),
    )

    name = models.CharField(max_length=100, verbose_name='Nombre')
    description = models.TextField(verbose_name='Descripción')
    m2_building = models.IntegerField(verbose_name='Metros cuadrados construidos')
    m2_total = models.IntegerField(verbose_name='Metros cuadrados totales')
    n_parking = models.IntegerField(verbose_name='Número de estacionamientos')
    n_bedrooms = models.IntegerField(verbose_name='Número de dormitorios')
    n_bathrooms = models.IntegerField(verbose_name='Número de baños')
    address = models.CharField(max_length=200, verbose_name='Dirección')
    comuna = models.ForeignKey(Comuna, on_delete=models.DO_NOTHING, verbose_name='Comuna')
    ptype = models.SmallIntegerField(choices=TYPE_CHOICES, verbose_name='Tipo', default=0)
    price = models.IntegerField(verbose_name='Precio')
    landlord = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Arrendador', null=True, blank=True)
    picture = models.ImageField(upload_to='properties', verbose_name='Imagen', null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)

    @property
    def region(self):
        return self.comuna.cod_provincia.cod_region.nombre
    
    @property
    def get_picture(self):
        if self.picture:
            return f'{MEDIA_URL}{self.picture}'
        return f'{STATIC_URL}images/property-placeholder.jpg'

    def __str__(self):
        return f'{self.get_ptype_display()} {self.name}'
    
class Request(models.Model):
    origin_property = models.ForeignKey(Property, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    message = models.TextField()
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user} - {self.origin_property.name}'

class Contract(models.Model):
    origin_request = models.ForeignKey(Request, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    start_date = models.DateField()
    end_date = models.DateField()
    price = models.IntegerField(null=True, blank=True)
    status = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.origin_request.user.get_full_name()} - {self.origin_request.origin_property.name}'
