from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views import View
from .models import Product, Category, Bill, Detail
from clientes.models import Client
from django.core.paginator import Paginator
from django.core.mail import send_mail
from django.contrib.auth.decorators import login_required
# Create your views here.

class Catalog(View):

	def view_catalog(request):
		products = Product.objects.all()
		paginator = Paginator(products, 15)
		page = request.GET.get('page')
		products = paginator.get_page(page)
		if request.user.is_authenticated:
			contexto = { 'productos': products, 'categoria' : "All", 'email' : user_activate(request.user.id),
			'num_product' : total_detail(request.user.id), 'details' : view_details(request.user.id) }
		else:
			contexto = { 'productos': products, 'categoria' : "All" }
		return render(request, 'productos/catalogue.html', contexto )


	def view_category_catalog(request, categoria):
		category = Category.objects.get(name=categoria)
		products = Product.objects.all().filter(category=category)
		paginator = Paginator(products, 15)
		page = request.GET.get('page')
		products = paginator.get_page(page)
		if request.user.is_authenticated:
			contexto = { 'categoria' : category, 'productos' : products, 'email' : user_activate(request.user.id) }
		else:
			contexto = { 'categoria' : category, 'productos' : products }
		return render(request, 'productos/catalogue.html', contexto )


class shopping_cart(View):
		
		def view_shopping_cart(request):
			if request.user.is_authenticated:
				client = Client.objects.get(client=request.user.id)	
				bill = Bill.objects.get(client=client, status="new")
				details = Detail.objects.filter(bill=bill)
				total = calculate_total(details)
				contexto = { 'cliente' : client, 'factura' : bill, 'detalles' : details, 'total' : total, 'num_product' : details.count() }
				return render(request, 'productos/cart.html', contexto )
			else:
				return render(request, 'productos/cart.html' )

		@login_required(login_url='/client/login/')
		def add_cart(request, id_product):
			client = Client.objects.get(client=request.user.id)
			bill = Bill.objects.get(client=client, status="new")
			product = Product.objects.get(id=id_product)
			detail = Detail(bill=bill, Product=product, description="Compra 1")
			detail.save()
			return redirect('/product/cart')

		@login_required(login_url='/client/login/')
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
			bill = Bill(client=client, status = "new")
			bill.save()
			return redirect('/product/cart')

		def update_cart(request, ids, cantidades):
			ids = ids.split('-')
			cantidades = cantidades.split('-')
			tama = len(ids)
			for i in range(tama):
				detail = Detail.objects.get(pk=ids[i])
				detail.quantity = cantidades[i]
				detail.save()
			return redirect('/product/cart')


		
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

def user_activate(idUser):
	client = Client.objects.get(client=idUser)
	return str(client.client.email)

def Index(request):
	if request.user.is_authenticated:
		return render(request, 'productos/index.html', { 'email' : user_activate(request.user.id),
		 'num_product' : total_detail(request.user.id), 'details' : view_details(request.user.id) })
	else:
		return render(request, 'productos/index.html')

def About(request):
	if request.user.is_authenticated:
		return render(request, 'productos/about.html', { 'email' : user_activate(request.user.id),
		 'num_product' : total_detail(request.user.id), 'details' : view_details(request.user.id) })
	else:
		return render(request, 'productos/about.html')

def Contact(request):
	if request.user.is_authenticated:
		return render(request, 'productos/contact.html', { 'email' : user_activate(request.user.id),
		'num_product' : total_detail(request.user.id), 'details' : view_details(request.user.id) })
	else:
		return render(request, 'productos/contact.html')

def total_detail(idUser):
	client = Client.objects.get(client=idUser)
	bill = Bill.objects.get(client=client, status="new")
	details = Detail.objects.filter(bill=bill).count()
	return details

def view_details(idUser):
	client = Client.objects.get(client=idUser)
	bill = Bill.objects.get(client=client, status="new")
	details = Detail.objects.filter(bill=bill)
	print(details)
	return details
