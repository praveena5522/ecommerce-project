from django.contrib import admin

from shop.models import Pet, PetCategory

# Register your models here.
admin.site.register(PetCategory)
admin.site.register(Pet)