from django.db import models

# Create your models here.
from django.db import models

class PetCategory(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name


class Pet(models.Model):
    CATEGORY = models.ForeignKey(PetCategory, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='pet_images/',default='pet_images/default.jpg')
    description = models.TextField()
    breed = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    age = models.PositiveIntegerField()
    size = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.name}"

class Cart(models.Model):
    cart_id = models.CharField(max_length=100, unique=True)


class CartItem(models.Model):
    CART = models.ForeignKey(Cart, on_delete=models.CASCADE)
    PET =models.ForeignKey(Pet, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    created_at = models.DateTimeField(auto_now_add=True)

class BuyAddress(models.Model):
    USER = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    address = models.TextField()
    phone = models.CharField(max_length=20)
    pincode = models.CharField(max_length=10)
    payment_method = models.CharField(max_length=50)


class orders(models.Model):
    ADDRESS = models.ForeignKey(BuyAddress, on_delete=models.CASCADE)
    PRODUCT = models.ForeignKey(Pet, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField(default=1)
    created_at = models.DateTimeField(auto_now_add=True)
    order_status = models.CharField(max_length=50, default='Pending')

    