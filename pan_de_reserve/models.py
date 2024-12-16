from django.db import models
import uuid

# Create your models here.
#$ pip install pillow  # pipenvを利用している場合は pipenv install pillow

from django.db import models

# Create your models here.

from django.db import models

class Allergy(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class BakeryItem(models.Model):
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name

class BakeryItemAllergy(models.Model):
    bakery_item = models.ForeignKey(BakeryItem, on_delete=models.CASCADE)
    allergy = models.ForeignKey(Allergy, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.bakery_item.name} - {self.allergy.name}"

class Reservation(models.Model):
    receive_time = models.DateTimeField()
    customer_name = models.CharField(max_length=255)
    customer_phone_number = models.CharField(max_length=20)
    is_received = models.BooleanField()

    def __str__(self):
        return f"Reservation for {self.customer_name} at {self.receive_time}"

class ReservationDetail(models.Model):
    reservation = models.ForeignKey(Reservation, on_delete=models.CASCADE)
    bakery_item = models.ForeignKey(BakeryItem, on_delete=models.CASCADE)

    def __str__(self):
        return f"Reservation {self.reservation.id} - {self.bakery_item.name}"

class LoginData(models.Model):
    username = models.TextField(default="root", null=False)
    password = models.TextField(default="password", null=False)

    def __str__(self):
        return self.username
