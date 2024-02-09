from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from .models import Order, OrderedItem
from products.models import Product
from .models import Customer  # Assuming Customer is your model for user profiles


# Create your views here.
def show_cart(request):
    user = request.user
    customer = user.customer_profile
    cart_obj,created = Order.objects.get_or_create(
        owner = customer,
        order_status = Order.CART_STAGE
    )

    context = {'cart' : cart_obj}
    return render(request,'shopping-cart.html',context)

def add_to_cart(request):
   
        user = request.user
        customer = user.customer_profile

        quantity = int(request.POST.get('quantity'))
        product_id = request.POST.get('product_id')

        cart_obj, created = Order.objects.get_or_create(
            owner=customer,
            order_status=Order.CART_STAGE
        )

        product = Product.objects.get(pk=product_id)

        ordered_item,created = OrderedItem.objects.get_or_create(
            product=product,
            owner=cart_obj,
            #quantity=quantity
        )
        if created :
              ordered_item.quantity=quantity
              ordered_item.save()

        else:
              ordered_item.quantity=ordered_item.quantity+quantity
              ordered_item.save()

        return redirect('cart')
    

def remove_item_from_cart(request,pk):
     
    item = OrderedItem.objects.get(pk=pk)
    if item:
            
        item.delete()
    return redirect('cart')



def checkout_cart(request):
    if request.POST:
        try:
            user = request.user
            customer = user.customer_profile

            total = float(request.POST.get('total'))
            

            order_obj, created = Order.objects.get(
                owner=customer,
                order_status=Order.CART_STAGE
            )
            if order_obj:
                order_obj.order_status = Order.ORDER_CONFIRMED
                order_obj.save()
                status_message = "your order is processed. your order will deliver soon"
                messages.success(request,status_message)
            else:
                status_message = "No order is processed, unable to proceed."
                messages.error(request,status_message)

        except Exception as e:
            status_message = "your order is processed. your order will deliver soon."
            messages.error(request,status_message)
    return redirect('shop')