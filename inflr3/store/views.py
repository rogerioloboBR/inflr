from django.shortcuts import render, get_object_or_404
from .models import Product
# Create your views here.


def home(request):
    products = Product.objects.all()
    template_name = 'store/home.html'
    context = {
        'products': products
    }
    
    return render(request, template_name, context)


def details(request, slug):

    product = get_object_or_404(Product, slug=slug)
    context = {
        'product': product
    }
    template_name = 'store/details.html'
    return render(request, template_name, context)


def productlist(request):
    products = Product.objects.all()
    template_name = 'store/productslist.html'
    context = {
        'products': products
    }
    return render(request, template_name, context)

def addproduct(request):

    template_name = 'store/addproduct.html'

    return render(request, template_name)