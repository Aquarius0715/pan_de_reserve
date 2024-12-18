from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = 'webapp'

urlpatterns = [
	path('', views.index, name="index"),
	path('nyuryoku/', views.nyuryoku, name="nyuryoku"),
	path('result/', views.result, name="result"),
    path('ReserveList/',views.ReserveList,name="ReserveList"),
]+ static(settings.STATIC_URL, document_root=settings.MEDIA_ROOT)