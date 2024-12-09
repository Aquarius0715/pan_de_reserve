from django.shortcuts import render, redirect
from .forms import LoginForm
from .models import LoginData


def index(request):
    return render(request, 'pan_de_reserve/index.html')


def nyuryoku(request):
    return render(request, 'pan_de_reserve/nyuryoku.html')


def result(request):
    return render(request, 'pan_de_reserve/result.html')


def ReserveList(request):
    return render(request, 'pan_de_reserve/ReserveList.html')


def login_view(request):
    error_message = ""
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]

            # データベースの認証
            try:
                user = LoginData.objects.get(username=username, password=password)
                return redirect("adminIndex")  # 認証成功 -> メインページへ
            except LoginData.DoesNotExist:
                error_message = "ユーザー名またはパスワードが間違っています。"

    else:
        form = LoginForm()

    return render(request, "pan_de_reserve/login.html", {"form": form, "error_message": error_message})


def admin_index(request):
    return render(request, "pan_de_reserve/adminIndex.html")
