from django.shortcuts import render,redirect

from shop.models import Cart, CartItem, Pet

from django.contrib.auth import authenticate, login,logout
from django.contrib.auth.models import User

# Create your views here.
def cart_id(request):
    cart_id = request.session.session_key
    if not cart_id:
        cart_id = request.session.create()
        cart_id = request.session.session_key
    return cart_id

def cart_item(request):
    c_id = cart_id(request)
    cart = Cart.objects.get(cart_id=c_id)
    cart_items = CartItem.objects.filter(CART=cart)
    return cart_items
    


def home1(request):
    cart_items = cart_item(request)
    pets = Pet.objects.all().order_by('-id')[:4]
    return render(request,"index.html", {"pets": pets, "cart_items": cart_items})

def allpets(request):
    pets = Pet.objects.all().order_by('-id')
    return render(request,"allpets.html", {"pets": pets})

def login1(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('home')
        else:
            return render(request,"login.html",{'error': 'Invalid username or password'})


    return render(request,"login.html")

def register(request):
    if request.method == 'POST':
        fname = request.POST['firstname']
        lname = request.POST['lastname']
        email = request.POST['email']
        uname = request.POST['username']
        pass1 = request.POST['password']
        pass2 = request.POST['confirm_password']
        if pass1 != pass2:
            return render(request,"register.html", {"error": "Passwords do not match"})
        if User.objects.filter(username=uname).exists():
            return render(request,"register.html", {"error": "Username already exists"})
        if User.objects.filter(email=email).exists():
            return render(request,"register.html", {"error": "Email already exists"})
        
        user = User.objects.create_user(username=uname, email=email, password=pass1, first_name=fname, last_name=lname)
        user.save()
        return redirect('login')
    return render(request,"register.html")


def logout1(request):
    logout(request)
    return redirect('home')

def detailes1(request,p_id):
    pet = Pet.objects.get(id=p_id)
    return render(request,"detailes.html", {"pet": pet})


def cart_id(request):
    cart_id = request.session.session_key
    if not cart_id:
        cart_id = request.session.create()
        cart_id = request.session.session_key
    return cart_id

def add_to_cart(request, p_id):
    pet = Pet.objects.get(id=p_id)
    c_id = cart_id(request)
    try:
        cart = Cart.objects.get(cart_id=c_id)
    
    except:
        cart = Cart.objects.create(cart_id=c_id)
        cart.save()

    
    try:
        cart_item = CartItem.objects.get(PET=pet, CART=cart)
        cart_item.quantity += 1
        cart_item.save()
    except:
        cart_item = CartItem.objects.create(PET=pet, CART=cart, quantity=1)
        cart_item.save()

    return redirect("home")

    
