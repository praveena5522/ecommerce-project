from django.shortcuts import render,redirect

from shop.models import Pet

from django.contrib.auth import authenticate, login,logout
from django.contrib.auth.models import User

# Create your views here.
def home1(request):
    return render(request,"index.html")

def allpets(request):
    pets = Pet.objects.all()
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
