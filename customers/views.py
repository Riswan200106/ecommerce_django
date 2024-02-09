from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from .models import Customer


# Create your views here.
def cust_account(request):
   
    return render(request,'customer_account.html')



def signout(request):
    logout(request)
    return redirect('/')

def account(request):
    context = {}
    if request.POST and 'register' in request.POST:
        context['register'] = True
        try:
            username= request.POST.get('username')
            password= request.POST.get('password')
            email= request.POST.get('email')
            address= request.POST.get('address')
            phone= request.POST.get('phone')

            #create user accounts
            user = User.objects.create_user(
                username=username,
                password=password,
                email = email
            )

            #create customer account
            customer = Customer.objects.create(
                user = user,
                phone = phone,
                address = address
                
            )

            success_message = "You have registered successfully..."
            messages.success(request,success_message)

        except Exception as e:
            error_message = "duplicate username or inavlid input"
            messages.error(request,error_message)

    if request.POST and 'login' in request.POST:
        context['register'] = False
        username= request.POST.get('username')
        password= request.POST.get('password')

        user = authenticate(username=username,password=password)
        if user:
            login(request,user)
            return redirect('index')
        else:
            messages.error(request,'invalid user credentials')

    return render(request,'account.html',context)