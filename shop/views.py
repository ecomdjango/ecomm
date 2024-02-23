#from contextlib import _RedirectStream
from django.shortcuts import render, redirect
from .models import Product, Commande, Category,Customer
from django.core.paginator import Paginator  
from django.shortcuts import render, redirect
from django.contrib.auth.hashers import make_password
from django.shortcuts import render , redirect , HttpResponseRedirect
from django.views import View
from django.contrib.auth.hashers import  check_password
from django.shortcuts import render, redirect

# Create your views here.
def index(request):
    product_object = Product.objects.all()
    item_name = request.GET.get('item-name')
    if item_name !='' and item_name is not None:
        product_object = Product.objects.filter(title__icontains=item_name)
    paginator = Paginator(product_object, 4)
    page = request.GET.get('page')
    product_object = paginator.get_page(page)
    return render(request, 'shop/index.html', {'product_object': product_object})

def detail(request, myid):
    product_object = Product.objects.get(id=myid)
    return render(request, 'shop/detail.html', {'product': product_object})

def checkout(request):
    if request.method == "POST":
        items = request.POST.get('items')
        total = request.POST.get('total')
        nom = request.POST.get('nom')
        email = request.POST.get('email')
        address = request.POST.get('address')
        ville = request.POST.get('ville')
        pays = request.POST.get('pays')
        zipcode = request.POST.get('zipcode')
        com = Commande(items=items, total=total, nom=nom, email=email, address=address, ville=ville, pays=pays, zipcode=zipcode)
        com.save()
        return redirect('confirmation')
        
        
    return render(request, 'shop/checkout.html')

def confirmation(request):
    info = Commande.objects.all()[:1]
    for item in info:
        nom = item.nom
    return render(request, 'shop/confirmation.html', {'name': nom})

def category(request):
    categories = Category.objects.all() 
    return render(request, 'shop/base.html', {'categories': categories})




class Signup(View):
    def get(self, request):
        return render(request, 'shop/inscription.html')

    def post(self, request):
        postData = request.POST
        fname = postData.get('fname')
        adresse = postData.get('adresse')
        phone = postData.get('phone')

        email = postData.get('email')
        username = postData.get('username')
        password = postData.get('password')
        # validation
        value = {

            'fname': fname,
            'adresse': adresse,
            'phone': phone,
            'username': username,
            'email': email,
            'password': password
        }
        error_message = None

        customer = Customer(
            fname=fname,
            adresse=adresse,
            phone=phone,
            username=username,
            email=email,
            password=password)
        error_message = False

        if not error_message:
            print(username, email, password)
            customer.password = make_password(customer.password)
            customer.register()
            return redirect('login.html')
        else:
            data = {
                'error': error_message,
                'values': value
            }
            return render(request, 'inscription.html', data)

        return error_message


from django.http import HttpResponse
class Login(View):
    return_url = None


    def get(self, request):
        Login.return_url = request.GET.get ('return_url')
        return render (request, 'shop/login.html')


    def post(self,request):
        # Fetch the first product from the database (you can modify this logic based on your needs)

        if request.method == 'POST':
            email = request.POST.get('email')
            password = request.POST.get('password')
            customer = Customer.get_customer_by_email(email)
            error_message = None
            if customer:
                flag = check_password(password, customer.password)
                if flag:
                    request.session['Customer'] = customer.id

                    if Login.return_url:
                        return HttpResponseRedirect(Login.return_url)
                    else:
                        Login.return_url = None
                        return redirect('home')
                else:
                    error_message = 'Invalid !password!'
            else:
                error_message = 'Invalid !email !'

            print(email, password)
            return render(request, 'shop/login.html', {'error': error_message})




