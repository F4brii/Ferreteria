from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from .models import Product, Category, Bill, Detail
from clientes.models import Client
# Create your views here.

class Catalog(View):

	def view_catalog(request):
		productos = Product.objects.all()
		contexto = { 'productos': productos }
		return render(request, 'productos/general.html', contexto )


	def view_category_catalog(request, categoria):
		category = Category.objects.get(name=categoria)
		products = Product.objects.all().filter(category=category)
		contexto = { 'categoria' : category, 'productos' : products }
		return render(request, 'productos/categoria.html', contexto )


class shopping_cart(View):
		
		def view_shopping_cart(request):
			client = Client.objects.get(client=request.user.id)
			bill = Bill.objects.get(client=client, status="new")
			detail = Detail.objects.filter(bill=bill)
			print('Aqui llegue')
			#total = self.calculate_total(detalles)
			contexto = { 'cliente' : client, 'factura' : bill, 'detalles' : detail }
			return render(request, 'productos/carrito.html', contexto )

		def calculate_total(self, detalles):
			total = 0
			print(total)
			for detalle in detalles:
				total = total + detalle.Product.price
			return total