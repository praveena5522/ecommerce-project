from django.shortcuts import render

from shop.models import Pet

# Create your views here.
def home1(request):
    return render(request,"index.html")

def allpets(request):
    pets = Pet.objects.all()
    return render(request,"allpets.html", {"pets": pets})

def login(request):
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

    return render(request,"register.html")
