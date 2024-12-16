from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = 'webapp'

urlpatterns = [
    path('', views.index, name="index"),
    path('login/', views.login_view, name="login"),
    path('nyuryoku/', views.nyuryoku, name="nyuryoku"),
    path('result/', views.result, name="result"),
    path('ReserveList/', views.ReserveList, name="ReserveList"),
    path('adminIndex/', views.admin_index, name="adminIndex"),
]+ static(settings.STATIC_URL, document_root=settings.MEDIA_ROOT)
