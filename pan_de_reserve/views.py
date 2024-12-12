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
            if quantities[i] != '0':
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
    insert_reservation_sql = """INSERT INTO pan_de_reserve_reservation VALUES (?, ?, ?, ?, ?)"""
    insert_reservation_detail_sql = """INSERT INTO pan_de_reserve_reservationdetail VALUES (?, ?, ?, ?)"""
    message = ""
    
    if (request.method == 'POST'):
        this_uuid = uuid.uuid4()
        print(this_uuid)
        orders = request.POST['order'].split()
        pans = []
        quantities = []
        for order in orders:
            tmp = order.split("×")
            num = int(str(tmp[1])[0:-1])
            if num != 0:
                pans.append(tmp[0])
                quantities.append(num)
        pan_sql = "SELECT id FROM pan_de_reserve_bakeryitem WHERE name = ?"
        pan_ids = []
        for pan in pans:
            pan_name_params = (pan,
            )
            results = db.query(pan_sql,pan_name_params)
            pan_ids.extend([re[0] for re in results])

        params = (
        request.POST['receive_time'],  # 受取時間
        request.POST['customer_name'],             # 顧客名
        request.POST['customer_phone_number'],        # 電話番号
        0,                  # 受取状況
        str(this_uuid).replace('-',''),
        )
        try:
            rows_affected = db.execute(insert_reservation_sql, params)
            print(f"新しい予約を {rows_affected} 件追加しました")
            if rows_affected == -1:
                print("rows affected = ",rows_affected)
                print("ERROR!!")
                print(request.POST)
                message = "正しく再入力してください"
            else:
                pass
                # return render(request, 'pan_de_reserve/result.html')
        except Exception as e:
            print(f"予期せぬエラー:{e}")
            print("ERROR number 1!")
            print(request.POST)
            message = "正しく再入力してください"
        for obj in Reservation.objects.all():
            print(obj)
        try:
            flag = -1
            for i in range(len(pan_ids)):
                flag = 0
                new_uuid = uuid.uuid4()
                params = (
                    pan_ids[i],
                    str(this_uuid).replace('-',''),
                    quantities[i],
                    str(new_uuid).replace('-',''),
                )
                rows_affected = db.execute(insert_reservation_detail_sql,params)
                print(f"新しい予約詳細を {rows_affected} 件追加しました")
                if rows_affected == -1:
                    print("ERROR!!")
                    print(request.POST)
                    message = "正しく再入力してください"
                    break
                else:
                    flag = 1
            if flag == 1:
                return render(request, 'pan_de_reserve/result.html')
        except:
            print("ERROR number 2!!")
            print(request.POST)
            message = "正しく再入力してください"            


    modelform_dict = {
        "msg":message,
        "form1": ReservationAdd(),
        "form2": ReservationDetailAdd(),
        "pans":request.POST['order'],
    }

    return render(request, 'pan_de_reserve/nyuryoku.html',modelform_dict)

def result(request):
    return render(request, 'pan_de_reserve/result.html')

def ReserveList(request):
    return render(request,'pan_de_reserve/ReserveList.html')

