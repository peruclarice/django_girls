from django.shortcuts import render, redirect
from products.models import *
from .forms import ProductForm
from django.core import serializers
from django.http import JsonResponse

# Create your views here.

def get_all_products(request):
    # get all products in db
    products = ProductModel.objects.all()
    return render(request, "products.html", {"products": products})

def get_product_by_id(request, id):
    product = None
    try:
        product = ProductModel.objects.get(id=id)
    except ProductModel.DoesNotExist:
        product = None
    return render(request, "single_product.html", {"single_product": product})

def create_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('product_list') # Replace 'product_list' with the name of your product list view
    else:
        form = ProductForm()
    return render(request, 'create_product.html', {'form': form})

def get_all_products_json(request):
    products = ProductModel.objects.all()
    json_data = serializers.serialize("json", products)
    print(json_data)
    return JsonResponse({"results":json_data})
