from django.urls import path
from shop.views import index, detail, checkout, confirmation, category,Signup,Login, commandes, categoryPage
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('', index, name='home'),
    path('', index, name='product'),
    path('commandes', commandes, name='commandes'),
    path('<int:myid>', detail, name="detail"),
    path('checkout', checkout, name="checkout"),
    path('confirmation', confirmation, name="confirmation" ),
    path('category', category, name="category" ),
    path('inscription', Signup.as_view(), name='inscription.html'),
    path('login', Login.as_view(), name='login.html'),
    path("logout/", LogoutView.as_view(), name="logout"),
    path('<slug:cat>', categoryPage, name="category"),

]
