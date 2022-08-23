from django.urls import path
from .import views

app_name = 'shop'

urlpatterns = [
	path('', views.Shop, name='shop'),
	path('products/', views.Products, name='products'),
	path('productdetail/<slug:product><int:pk>/', views.ProductDetail, name='product-detail'),
]
