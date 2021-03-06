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
from productos.views import Catalog, shopping_cart, Index, About, Contact
from clientes.views import Activity_User, das
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('das/', das),
    path('admin/', admin.site.urls),
    path('index/', Index, name = 'index'),
    path('product/', include([
    		path('', Catalog.view_catalog, name='general'),
    		path('category/<str:categoria>/', Catalog.view_category_catalog, name='category'),
    		path('cart/', shopping_cart.view_shopping_cart, name='cart'),
    		path('addcart/<int:id_product>/', shopping_cart.add_cart, name='addcart'),
    		path('paycart/', shopping_cart.pay_cart, name='pay'),
            path('update/<slug:ids>/<slug:cantidades>/', shopping_cart.update_cart, name = 'update'),
    	])),
    path('about/', About, name = 'acerca'),
    path('client/', include([
    		path('bills/', Activity_User.view_bill),
    		path('bills/detail/<int:id_bill>/', Activity_User.view_detail),
    		path('bills/pdf/', Activity_User.create_Pdf),
    		path('login/', Activity_User.sing_in, name = 'login'),
    		path('logout/', Activity_User.logout, name ='cerrar'),
    		path('update/', Activity_User.updateUser),
    		path('create/', Activity_User.createUser),
    		path('contact/', Activity_User.contactUser),
    	])),
    path('contact/', Contact, name = 'contacto'),
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
