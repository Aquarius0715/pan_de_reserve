from django.urls import path
from . import views

urlpatterns = [
	path('', views.index, name="index"),
	path('nyuryoku/', views.nyuryoku, name="nyuryoku"),
	path('result/', views.result, name="result"),
    path('ReserveList/',views.ReserveList,name="ReserveList"),
]