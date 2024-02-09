from django.urls import path
from . import views


urlpatterns = [
        path('cust_account/',views.cust_account,name='cust_account'), 
        #path('register/',views.register,name='register'), 
        #path('login/',views.loginn,name='login'), 
        path('logout/',views.signout,name='logout'), 
        path('account/',views.account,name='account'), 
]