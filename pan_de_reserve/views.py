from django.shortcuts import render
from django.views import View

def index(request):
    return render(request, 'pan_de_reserve/index.html')

def nyuryoku(request):
    return render(request, 'pan_de_reserve/nyuryoku.html')

def result(request):
    return render(request, 'pan_de_reserve/result.html')

def ReserveList(request):
    return render(request,'pan_de_reserve/ReserveList.html')
    
