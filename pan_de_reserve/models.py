from django.db import models
import uuid

# Create your models here.
#$ pip install pillow  # pipenvを利用している場合は pipenv install pillow

class Allergy(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class BakeryItem(models.Model):
    name = models.CharField(max_length=255,verbose_name="名前")
    price = models.DecimalField(max_digits=10, decimal_places=2,verbose_name="価格")
    image = models.ImageField(upload_to='images/',null=True,blank=True,verbose_name="商品画像")

    def __str__(self):
        return self.name

class BakeryItemAllergy(models.Model):
    bakery_item = models.ForeignKey(BakeryItem, on_delete=models.CASCADE)
    allergy = models.ForeignKey(Allergy, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.bakery_item.name} - {self.allergy.name}"

class Reservation(models.Model):
    id = models.UUIDField(primary_key=True,default=uuid.uuid4 ,editable=False)
    receive_time = models.DateTimeField(verbose_name="受取時間")
    customer_name = models.CharField(max_length=255,verbose_name="名前")
    customer_phone_number = models.CharField(max_length=20,verbose_name="電話番号")
    is_received = models.BooleanField(default=False)

    def __str__(self):
        return f"Reservation for {self.customer_name} at {self.receive_time}"

class ReservationDetail(models.Model):
    id = models.UUIDField(primary_key=True,default=uuid.uuid4,editable=False)
    reservation = models.ForeignKey(Reservation, on_delete=models.CASCADE)
    bakery_item = models.ForeignKey(BakeryItem, on_delete=models.CASCADE)
    quantity = models.DecimalField(max_digits=10, decimal_places=2,verbose_name="個数")

    def __str__(self):
        return f"Reservation {self.reservation.id} - {self.bakery_item.name}(x{self.quantity})"
