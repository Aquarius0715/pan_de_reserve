from django.shortcuts import render,redirect
from django.views import View
from .models import *
from .forms import *

def index(request):
    pans = BakeryItem.objects.values()
    allergy = BakeryItemAllergy.objects.values()
    dicts = {
        'pans' : pans,
        'allergy' : allergy,        
    }
    return render(request, 'pan_de_reserve/index.html',dicts)

def nyuryoku(request):
    print(request.method)
    message = ''  # 初期表示ではカラ
    if (request.method == 'POST'):
        form = ReservationAdd(request.POST)
        print(form.is_valid())
        print(form)
        if form.is_valid():
            form.save()
            print("saved!")
            return redirect(to='/result')
        else:
            message = '再入力して下さい'
    modelform_dict = {
        "form1": ReservationAdd(),
        "form2": ReservationDetailAdd(),
    }

    return render(request, 'pan_de_reserve/nyuryoku.html',modelform_dict)

def result(request):
    return render(request, 'pan_de_reserve/result.html')

def ReserveList(request):
    return render(request,'pan_de_reserve/ReserveList.html')

