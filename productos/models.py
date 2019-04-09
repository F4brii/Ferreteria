from django.db import models
from clientes.models import Client
from datetime import date
# Create your models here.

class Category(models.Model):
	name = models.CharField("Nombre", max_length=50)
	description = models.TextField("Descripcion")

	def __str__(self):
   		return self.name


class Product(models.Model):
	image = models.ImageField("Imagen_Producto", upload_to='Productos')
	price = models.IntegerField("Precio", default=0)
	description = models.TextField("Descripcion", max_length=500)
	category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name="Categoria")

	def __str__(self):
   		return self.description


class Bill(models.Model):
	client = models.ForeignKey(Client, on_delete=models.CASCADE, verbose_name="Cliente")
	date = models.DateField("Fecha", default=date.today)
	status = models.CharField("Estado_Factura", default = 'new', max_length=50)

	def __str__(self):
   		return self.status


class Detail(models.Model):
	bill = models.ForeignKey(Bill, on_delete=models.CASCADE, verbose_name="Factura")
	Product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name="Producto")
	description = models.TextField("Descripcion", max_length=500)
	quantity = models.IntegerField("Cantidad", default = 1)

	def __str__(self):
   		return self.description


		
		

		
