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
