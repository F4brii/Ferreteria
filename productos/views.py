from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views import View
from .models import Product, Category, Bill, Detail
from clientes.models import Client

from django.core.mail import send_mail
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
			details = Detail.objects.filter(bill=bill)
			total = calculate_total(details)
			contexto = { 'cliente' : client, 'factura' : bill, 'detalles' : details, 'total' : total }
			return render(request, 'productos/carrito.html', contexto )

		def add_cart(request, id_product):
			client = Client.objects.get(client=request.user.id)
			bill = Bill.objects.get(client=client, status="new")
			product = Product.objects.get(id=id_product)
			detail = Detail(bill=bill, Product=product, description="Compra 1")
			detail.save()
			return redirect('/product/cart')

		def pay_cart(request):
			client = Client.objects.get(client=request.user.id)	
			bill = Bill.objects.get(client=client, status="new")
			bill.status = "pagado"
			bill.save()
			details = Detail.objects.filter(bill=bill)
			send_mail(
    			'Asunto prueba',
    			create_string(details),
    			'fcaicedom28@gmail.com',
    			['fabricio.caicedo@unillanos.edu.co'],
    			fail_silently=False,
			)
			return HttpResponse("Pago")


		
def calculate_total(details):
	total = 0
	for detail in details:
		total = total + detail.Product.price
	return total

def create_string(details):
	list_products = "Factura de cobro Ferreterias S.A" +'\n\n'
	for detail in details:
		list_products = list_products + '\n' + "und. " + str(detail.quantity) + " " + detail.Product.description + " $" + str(detail.Product.price)
	total = calculate_total(details)
	list_products = list_products + '\n\n' + "Total a pagar: $" + str(total)
	return list_products

def Index(request):
	return render(request, 'productos/contact.html')