"""Ferreteria URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from productos.views import Catalog, shopping_cart
from clientes.views import Activity_User

urlpatterns = [
    path('admin/', admin.site.urls),
    path('product/', include([
    		path('', Catalog.view_catalog),
    		path('category/<str:categoria>/', Catalog.view_category_catalog),
    		path('cart/', shopping_cart.view_shopping_cart),
    		path('addcart/<int:id_product>/', shopping_cart.add_cart),
    		path('paycart/', shopping_cart.pay_cart),
    	])),
    path('client/', include([
    		path('bills/', Activity_User.view_bill),
    		path('bills/detail/<int:id_bill>/', Activity_User.view_detail),
    		path('bills/pdf/', Activity_User.create_Pdf),
    		path('login/', Activity_User.sing_in),
    		path('logout/', Activity_User.logout),
    	])),
]
