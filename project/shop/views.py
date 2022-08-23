from django.shortcuts import render, get_object_or_404
from .models import Product

# Create your views here.

def Shop(request):
	return render(request, 'shop/index/shop.html')

def Products(request):
	productsCount = Product.objects.all().count()
	products = Product.objects.all()
	return render(request, 'shop/products/productslist.html', {'products':products, 'productsCount':productsCount})

def ProductDetail(request, product, pk):
	product = get_object_or_404(Product, slug=product, id=pk)
	return render(request, 'shop/products/productdetail.html', {'product':product})
