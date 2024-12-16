from django.contrib import admin
from .models import *

# Register your models here.

class ReserveDeatils(admin.ModelAdmin):
    list_display = ('reservation_customer_name','bakery_item_name','quantity')

    def bakery_item_name(self,obj):
        return obj.bakery_item.name
    def reservation_customer_name(self,obj):
        return obj.reservation.customer_name

class Reservations(admin.ModelAdmin):
    list_display = ('receive_time','customer_name','customer_phone_number')


        
admin.site.register(BakeryItem)
admin.site.register(Reservation,Reservations)
admin.site.register(ReservationDetail,ReserveDeatils)
admin.site.register(BakeryItemAllergy)
admin.site.register(Allergy)

