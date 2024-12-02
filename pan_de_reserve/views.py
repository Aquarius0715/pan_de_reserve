from django.shortcuts import render
from django.views import View
from .models import *

def index(request):
    pans = BakeryItem.objects.values()
    allergy = BakeryItemAllergy.objects.values()
    dicts = {
        'pans' : pans,
        'allergy' : allergy,        
    }
    return render(request, 'pan_de_reserve/index.html',dicts)

def nyuryoku(request):
    return render(request, 'pan_de_reserve/nyuryoku.html')

def result(request):
    return render(request, 'pan_de_reserve/result.html')

def ReserveList(request):
    return render(request,'pan_de_reserve/ReserveList.html')

