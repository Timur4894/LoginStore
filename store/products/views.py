from django.shortcuts import render
from products.models import ProductCategory, Product

def index(request):
    context = {
        'title':'Store',
        'is_active': True,
    }
    return render(request, "products/index.html", context)

def products(request):
    context = {
        'title': 'Store',
        'products': Product.objects.all(),
        'category': ProductCategory.objects.all(),
    }
    return render(request, "products/products.html",context)


