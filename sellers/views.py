from django.shortcuts import render

from common.models import Seller
from sellers.models import Products
from customers.models import Order

# Create your views here.
def seller_home(request):
    seller = Seller.objects.get(seller_id=request.session['seller'])
    products = Products.objects.filter(seller_id=request.session['seller'])
    return render(request,'sellerhome.html',{'seller':seller,'product':products,})

def add_product(request):
    message = ""
    if request.method == "POST":
        name = request.POST["pname"]
        price = request.POST["pprice"]
        description = request.POST["pdescription"]
        product_stock = request.POST["pquantity"]
        image = request.FILES["pimg"]
        seller = Seller.objects.get(seller_id=request.session['seller']) #taking row(object) from table

        new_product = Products(product_name=name,price=price,description=description,stock=product_stock,product_image=image,seller_id=seller)
        new_product.save()

        message="Product Added Successfully!"
    return render(request, 'add_product.html' ,{'msg':message,})
  

def view_product(request):
    seller_product = Products.objects.filter(seller_id=request.session['seller'])
    return render(request,'view_products.html',{'products':seller_product})

def change_pw(request):
    msg = ""
    if request.method == "POST":
        oldpassword = request.POST['oldpw']
        newpassword = request.POST['newpw']
        confirmpassword = request.POST['cpw']

        seller_data = Seller.objects.get(seller_id=request.session['seller'])
        if oldpassword==seller_data.password:
            if newpassword==confirmpassword:
                seller_data.password=newpassword
                seller_data.save()
                msg = "Password Changed..!"
            else:
                msg = "Password Not Matching..!"
        else:
            msg = "Password Is Incorrect..!"
    return render(request,'change_password.html',{'message':msg,})

def view_order(request):
    orders = Order.objects.filter(seller_id=request.session['seller'], status="ordered")
    return render(request,'view_order.html',{'orders':orders,})