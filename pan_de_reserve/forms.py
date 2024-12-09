from django.forms import ModelForm,SplitDateTimeField,widgets
from .models import *

class ReservationAdd(ModelForm):
    class Meta:
        model = Reservation
        fields = ["receive_time","customer_name","customer_phone_number"]
        widgets = {"receive_time":widgets.SelectDateWidget}

class ReservationDetailAdd(ModelForm):
    class Meta:
        model = ReservationDetail
        fields = ["reservation","bakery_item","quantity"]