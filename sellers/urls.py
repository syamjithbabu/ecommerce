from django.urls import path
from . import views

app_name = 'sellers'

urlpatterns = [
    path('sellerhome',views.seller_home,name='sellershome'),
    path('add_product',views.add_product,name='addproduct'),
    path('viewproduct',views.view_product,name='sellerviewproduct'),
    path('changepw',views.change_pw,name="changepw"),
    path('vieworder',views.view_order,name="view_order")
]