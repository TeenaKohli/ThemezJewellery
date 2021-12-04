from django.shortcuts import render
from . models import Product

# Create your views here.

def store(request):
    products = Product.objects.all().filter()

    context = {
        'products': products,
    }
    return render(request, 'store/store.html', context)

def product_detail(request):
    return render(request,'store/product_detail.html')