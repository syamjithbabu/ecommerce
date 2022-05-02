from django.urls import path
from . import views

app_name = 'customers'

urlpatterns = [
    path('customerhome',views.customer_home,name='customerhome'),
    path('vieworder',views.view_order,name='vieworder'),
    path('viewcart',views.view_cart,name='viewcart'),
    path('changepw',views.change_pw,name="changepassword"),
    path('addtocart/<int:id>',views.add_to_cart,name="addtocart"),
    path('logout',views.logout,name="logout"),
    path('order/<int:pid>',views.order_product,name="orderproduct"),
    path('index',views.index,name='index')
]