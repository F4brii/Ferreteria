from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from .models import Client
from productos.models import Bill, Detail
from reportlab.pdfgen import canvas
from django.contrib.auth import authenticate, login, logout
# Create your views here.

class Activity_User(View):

	def view_bill(request):
		client = Client.objects.get(client=request.user.id)
		bills =  Bill.objects.filter(client = client)
		contexto = { 'bills' : bills }
		return render(request, 'clientes/facturas.html', contexto)

	def view_detail(request, id_bill):
		details = Detail.objects.filter(bill = id_bill)
		contexto = { 'details' : details }
		return render(request, 'clientes/detalles.html', contexto)

	def create_Pdf(request):
		client = Client.objects.get(client=request.user.id)
		bills =  Bill.objects.filter(client = client)
		create_pdf(bills)
		return HttpResponse("Se creo el pdf")

	def sing_in(request):
		username = "fabricio"
		password = "Assemblix86"
		user = authenticate(username=username, password=password)
		if user is not None:
			login(request, user)
			client = Client.objects.get(client=user)
			bill = Bill(client=client, status = "new")
			bill.save()
			return HttpResponse("Bienvenido")
		else:
			return HttpResponse("Error")

	def logout(request):
		client = Client.objects.get(client=request.user.id)
		bill = Bill.objects.get(client=client, status = "new")
		if(Detail.objects.filter(bill=bill).count() != 0):
			return HttpResponse("Tiene una transacion pendiente")
		else:
			bill.status = 'cancelado'
			bill.save()
			logout(request)
			return HttpResponse("cierre correcto")

def create_pdf(bills):
	x = 800
	c = canvas.Canvas("bills.pdf")
	for bill in bills:
		content = "Factura n. " + str(bill.id) + "\n Descripcion: " + bill.status
		c.drawString(0, x, content)
		c.drawString(0, x-20, '\n' + writer_str(bill))
		x-=40	
	c.showPage()
	c.save()


def writer_str(bill):
	msj = ""
	details = Detail.objects.filter(bill = bill)
	for detail in details:
		msj = msj + '\n' + str(detail.Product.id) + " " + detail.Product.description
	return msj+'\n\n'