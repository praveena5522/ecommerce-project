from django.shortcuts import render

from shop.models import Pet

# Create your views here.
def home1(request):
    return render(request,"index.html")

def allpets(request):
    pets = Pet.objects.all()
    return render(request,"allpets.html", {"pets": pets})
