from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('api/', views.API, name="API"),
    path('api/bydate', views.API_Posortowane_Data, name="API_Posortowane_Data"),
    path('api/avaible', views.API_TylkoDostepne, name="API_TylkoDostepne"),
    path('api/last', views.API_OstatniRekord, name="API_OstatniRekord")
]