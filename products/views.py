from django.shortcuts import render
from . models import Product
from django.core.paginator import Paginator

# Create your views here.
def index(request):
    return render(request,'index.html')




def shop(request):
    # Here we are adding the products through admin
    page = 1
    if request.GET:
        page = request.GET.get('page',1)
    product_list = Product.objects.all()
    product_paginator = Paginator(product_list,4)
    product_list = product_paginator.get_page(page)
    context = {'products': product_list}
    return render(request, 'shop.html', context)

def shop_details(request,pk):
    product = Product.objects.get(pk=pk)
    context ={'product' : product}
    return render(request,'product-details.html',context)

def cart(request):
    return render(request,'shopping-cart.html')
