from django.contrib import admin
from .models import *

# Register your models here.

admin.site.register(BakeryItem)
admin.site.register(Reservation)
admin.site.register(ReservationDetail)
admin.site.register(BakeryItemAllergy)
admin.site.register(Allergy)
