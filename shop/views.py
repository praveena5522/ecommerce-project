from django.shortcuts import render,redirect

from shop.models import Cart, CartItem, Pet

from django.contrib.auth import authenticate, login,logout
from django.contrib.auth.models import User
from django.core.paginator import Paginator

from django.db.models import Q

# Create your views here.
def cart_id(request):
    cart_id = request.session.session_key
    if not cart_id:
        cart_id = request.session.create()
        cart_id = request.session.session_key
    return cart_id

def cart_item(request):
    c_id = cart_id(request)
    cart, created = Cart.objects.get_or_create(cart_id=c_id)
    cart_items = CartItem.objects.filter(CART=cart)
    return cart_items
    


def home1(request):
    cart_items = cart_item(request)
    pets = Pet.objects.all().order_by('-id')[:4]
    return render(request,"index.html", {"pets": pets, "cart_items": cart_items})

def allpets(request):
    cart_items = cart_item(request)

    
    try:
        qry = request.GET['q']
        if qry:
            pets = Pet.objects.filter(Q(name__icontains=qry) | Q(description__icontains=qry)).order_by('-id')
        else:
            pets = Pet.objects.all().order_by('-id')
    except KeyError:
        pets = Pet.objects.all().order_by('-id')
    paginator = Paginator(pets,5)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    return render(request,"allpets.html", {"page_obj": page_obj, "cart_items": cart_items})

def login1(request):
    cart_items = cart_item(request)
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('home')
        else:
            return render(request,"login.html",{'error': 'Invalid username or password', "cart_items": cart_items})
    return render(request,"login.html", {"cart_items": cart_items})

def register(request):
    cart_items = cart_item(request)
    if request.method == 'POST':
        fname = request.POST['firstname']
        lname = request.POST['lastname']
        email = request.POST['email']
        uname = request.POST['username']
        pass1 = request.POST['password']
        pass2 = request.POST['confirm_password']
        if pass1 != pass2:
            return render(request,"register.html", {"error": "Passwords do not match", "cart_items": cart_items})
        if User.objects.filter(username=uname).exists():
            return render(request,"register.html", {"error": "Username already exists", "cart_items": cart_items})
        if User.objects.filter(email=email).exists():
            return render(request,"register.html", {"error": "Email already exists", "cart_items": cart_items})
        
        user = User.objects.create_user(username=uname, email=email, password=pass1, first_name=fname, last_name=lname)
        user.save()
        return redirect('login')
    return render(request,"register.html", {"cart_items": cart_items})


def logout1(request):
    logout(request)
    return redirect('home')

def detailes1(request,p_id):
    cart_items = cart_item(request)
    pet = Pet.objects.get(id=p_id)
    return render(request,"detailes.html", {"pet": pet, "cart_items": cart_items})


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

    
def minus_from_cart(request, p_id):
    pet1 = Pet.objects.get (id=p_id)
    cid = cart_id(request)
    cart1 = Cart.objects.get(cart_id=cid)
    cart_item = CartItem.objects.get(PET=pet1, CART=cart1)
    if cart_item.quantity == 1:
        cart_item.delete()
    else:
        cart_item.quantity -= 1
        cart_item.save()
    return redirect("home")

def remove_cart_item(request,p_id):
    pet = Pet.objects.get(id=p_id)
    cid = cart_id(request)
    cart = Cart.objects.get(cart_id=cid)
    cart_item = CartItem.objects.get(PET=pet, CART=cart)
    cart_item.delete()
    return redirect("home")