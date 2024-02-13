from django.urls import path
from shop.views import index, detail, checkout, confirmation, category

urlpatterns = [
    path('', index, name='home'),
    path('', index, name='product'),
    path('<int:myid>', detail, name="detail"),
    path('checkout', checkout, name="checkout"),
    path('confirmation', confirmation, name="confirmation" ),
    path('category', category, name="category" ),
]
