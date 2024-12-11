from django.shortcuts import render,redirect
from django.views import View
from .models import *
from .forms import *
from .SQLiteManager import * 
import uuid

def index(request):
    pans = BakeryItem.objects.values()
    allergy = BakeryItemAllergy.objects.values()
    if (request.method == 'POST'):
        print(request.POST)
        order_text = ""
        quantities = request.POST.getlist('quantity')
        for i in range(len(pans)):
            print(pans[i]['name'],quantities[i])
            if quantities[i] != 0:
                order_text += pans[i]['name'] + "×" + quantities[i] + "個\n"
        parms = {
            'order':order_text,
            'totalPrice':request.POST['totalPrice'],
        }
        print("parms = ",parms)
        return render(request, 'pan_de_reserve/nyuryoku.html',parms)
    dicts = {
        'pans' : pans,
        'allergy' : allergy,        
    }
    return render(request, 'pan_de_reserve/index.html',dicts)

def nyuryoku(request):
    db = SQLiteManager("db.sqlite3")

    sql_count = "SELECT COUNT(*) FROM pan_de_reserve_reservation"
    result = db.query(sql_count)
    total_reservations = result[0][0] if result else 0
    insert_sql = """INSERT INTO pan_de_reserve_reservation VALUES (?, ?, ?, ?, ?)"""
    message = ""
    
    if (request.method == 'POST'):
        print(request.POST)
        try:
            params = (
            total_reservations,
            request.POST['receive_time'],  # 受取時間
            request.POST['customer_name'],             # 顧客名
            request.POST['customer_phone_number'],        # 電話番号
            0                  # 受取状況
            )
            rows_affected = db.execute(insert_sql, params)
            print(f"新しい予約を {rows_affected} 件追加しました")
            if rows_affected == -1:
                print(request.POST)
            else:
                return render(request, 'pan_de_reserve/result.html')
        except:
            print("ERROR!!")
            print(request.POST)
            message = "正しく再入力してください"


    modelform_dict = {
        "msg":message,
        "form1": ReservationAdd(),
        "form2": ReservationDetailAdd(),
    }

    return render(request, 'pan_de_reserve/nyuryoku.html',modelform_dict)

def result(request):
    return render(request, 'pan_de_reserve/result.html')

def ReserveList(request):
    return render(request,'pan_de_reserve/ReserveList.html')

