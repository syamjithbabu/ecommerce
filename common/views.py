from django.shortcuts import redirect, render

from common.forms import CustomerRegForm, SellerRegForm
from . models import *

# Create your views here.
def home(requset):
    return render(requset,'mainpage.html')


#seller registration
def seller_reg(request):
    seller_msg =""
    form=SellerRegForm()

    if request.method == 'POST':
        form=SellerRegForm(request.POST)
        if form.is_valid():
            name = request.POST['cust_name']
            email = request.POST['email_id']
            acc_holder = request.POST['accholder']
            acc_no = request.POST['accno']
            ifsc = request.POST['ifsc']
            phoneno = request.POST['phone']
            password = request.POST['password']
            
            email_exist = Seller.objects.filter(email_id=email).exists()

            if not email_exist:
                new_customer = Seller(seller_name=name,email_id=email,acc_holder=acc_holder,acc_no=acc_no,ifsc=ifsc,phone_no=phoneno,password=password)
                new_customer.save()
                form=SellerRegForm()
                seller_msg = "registerd succesfully"
            else:
                seller_msg = "email already exists"
        else:
            print(form.errors)

    return render(request,'sellerreg.html',{'msg': seller_msg,'form':form,})

#seller login
def seller_login(request):
    seller_msg = ""
    if request.method == "POST":
        seller_name = request.POST['username']
        seller_password = request.POST['password']

        seller_exist = Seller.objects.filter(seller_name=seller_name,password=seller_password).exists()

        if seller_exist:
            seller_data = Seller.objects.get(seller_name=seller_name,password=seller_password) #by using get we get a single data
            request.session['seller'] = seller_data.seller_id
            return redirect('sellers:sellershome')
        else:
            seller_msg = 'Incorrect Password!'
    return render(request,'sellerlogin.html',{'seller_msg':seller_msg,})



#customer registration
def customer_reg(request):
    cust_msg =""
    form=CustomerRegForm()

    if request.method == 'POST':
        form=CustomerRegForm(request.POST)
        if form.is_valid():
            name = request.POST['cust_name']
            email = request.POST['email_id']
            phoneno = request.POST['phone_no']
            password = request.POST['password']
            
            email_exist = Customer.objects.filter(email_id=email).exists()

            if not email_exist:
                new_customer = Customer(cust_name=name,email_id=email,phone_no=phoneno,password=password)
                new_customer.save()
                form=CustomerRegForm()
                cust_msg = "registerd succesfully"
            else:
                cust_msg = "email already exists"
        else:
            print(form.errors)

    return render(request,'customerreg.html',{'msg': cust_msg,'form':form,})

def customer_login(request):
    message = ""
    if request.method == "POST":
        customer_name = request.POST['username']
        customer_password = request.POST['password']

        customer_exist = Customer.objects.filter(cust_name=customer_name,password=customer_password).exists()

        if customer_exist:
            customer_data = Customer.objects.get(cust_name=customer_name,password=customer_password)
            request.session['customer'] = customer_data.cust_id
            return redirect('customers:customerhome')
        else:
            message = 'Incorrect Password!'
            return render(request,'customerlogin.html',{'message':message,})
    return render(request,'customerlogin.html')

