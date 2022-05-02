from urllib import response
from django.http import HttpResponse
from django.shortcuts import redirect, render

from common.models import Customer, Seller
from ecommerce.decorators import auth_customer
from rest_framework.decorators import api_view
from sellers.models import Products
from customers.models import Cart, Order

from django.conf import settings
from django.core.mail import send_mail
from rest_framework.response import Response

# Create your views here.
@auth_customer
def customer_home(request):

    customers = Customer.objects.get(cust_id = request.session['customer'])
    products = Products.objects.all()
    return render(request,'customer_home.html',{'customer':customers,'product':products})
    

@auth_customer
def view_cart(request):
    return render(request,'cart.html')

def view_order(request):
    orders = Order.objects.filter(customer_id=request.session['customer'], status="ordered")
    return render(request,'view_order.html',{'orders':orders,})

def change_pw(request):
    msg = ""
    if request.method == "POST":
        oldpassword = request.POST['oldw']
        newpassword = request.POST['newpw']
        confirmpassword = request.POST['cpw']

        customer_data = Customer.objects.get(cust_id=request.session['customer'])
        if customer_data.password == oldpassword:
            if newpassword == confirmpassword:
                Customer.objects.filter(cust_id=request.session['customer']).update(password=newpassword)
                msg = "Password Changed..!"
            else:
                msg = "Password Not Matching..!"
        else:
            msg = "Password Is Incorrect..!"
    return render(request,'change_password.html',{'message':msg,})

def add_to_cart(request,id):
    product_id = Products.objects.get(p_id=id)
    customer_id = Customer.objects.get(cust_id=request.session['customer'])

    cart_exist = Cart.objects.filter(customer_id=request.session['customer'],product_id=product_id).exists()

    if not cart_exist:
        new_cart = Cart(customer_id=customer_id,product_id=product_id)
        new_cart.save()

    return redirect('customers:customerhome')

def view_cart(request):
    cart_products = Cart.objects.filter(customer_id=request.session['customer'])

    return render(request,'view_cart.html',{'cartproduct':cart_products,})

def logout(request):
    del request.session['customer']
    request.session.flush()

    return redirect('common:customerlogin')

def order_product(request,pid):
    msg = ""
    product = Products.objects.get(p_id=pid)

    if request.method == "POST":

        customer_id = Customer.objects.get(cust_id=request.session['customer'])
        seller_id = Seller.objects.get(seller_id=product.seller_id.seller_id)
        quantity = request.POST["quantity"]
        shipping_address = request.POST["address"]
        total_amount = int(quantity)*product.price

        order=Order(product_id=product,
        customer_id=customer_id,seller_id=seller_id,
        quantity=quantity,
        shipping_address=shipping_address,
        total_amount=total_amount)
        order.save()

        send_mail("order deatails","your order for ------- is placed successfully",settings.EMAIL_HOST_USER,[str(customer_id.email_id)])
        
        product.stock=product.stock-int(quantity)
        product.save()
        msg="orderd"
    return render(request,'order.html',{'msg':msg,'product':product})

@api_view(['GET'])
def index(request):
    message = 'Congratulations, you have created an API'
    return Response(message)