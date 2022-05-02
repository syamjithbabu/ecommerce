from django.urls import path
from . import views

app_name = 'common'

urlpatterns = [
    path('',views.home,name='homepage'),
    path('sellerreg',views.seller_reg,name='sellerreg'),
    path('sellerlogin',views.seller_login,name='sellerlogin'),
    path('customerreg',views.customer_reg,name='customerreg'),
    path('customerlogin',views.customer_login,name='customerlogin'),
    
]