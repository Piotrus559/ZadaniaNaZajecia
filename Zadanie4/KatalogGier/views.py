from django.shortcuts import render
from django.http import JsonResponse
from .models import Gra

def index(request):
    return render(request, 'KatalogGier/index.html')

def API(request):
    Obiekty = []
    Gry = Gra.objects.all()

    for g in Gry:
        Obiekty.append({
            "Tytuł": g.Tytul,
            "Data wydania": g.DataWydania,
            "Twórcy": g.Tworcy,
            "Wydawca": g.Wydawca,
            "Dostępna": g.Dostepna
        })
    
    return JsonResponse({
        "count": len(Obiekty),
        'items': Obiekty
    })