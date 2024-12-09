from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('login/', views.login_view, name="login"),
    path('nyuryoku/', views.nyuryoku, name="nyuryoku"),
    path('result/', views.result, name="result"),
    path('ReserveList/', views.ReserveList, name="ReserveList"),
    path('adminIndex/', views.admin_index, name="adminIndex"),
]
