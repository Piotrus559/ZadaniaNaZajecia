from django.shortcuts import render
from django.http import JsonResponse
from .models import Gra

def index(request):
    return render(request, 'KatalogGier/index.html')

def API(request):
    Gry = Gra.objects.all()
    Obiekty = ZwrocObiekty(Gry)
    
    return JsonResponse({
        'items': Obiekty
    })

def API_Posortowane_Data(request):
    Gry = Gra.objects.all().order_by("DataWydania")
    Obiekty = ZwrocObiekty(Gry)
    
    return JsonResponse({
        'items': Obiekty
    })

def API_TylkoDostepne(request):
    Gry = Gra.objects.all().filter(Dostepna=True)
    Obiekty = ZwrocObiekty(Gry)
    
    return JsonResponse({
        'items': Obiekty
    })

def API_OstatniRekord(request):
    Gry = Gra.objects.all().order_by('-id')[:1]
    Obiekty = ZwrocObiekty(Gry)
    
    return JsonResponse({
        'items': Obiekty
    })

def ZwrocObiekty(gry):
    O = []
    for g in gry:
        O.append({
            "Tytuł": g.Tytul,
            "Data wydania": g.DataWydania,
            "Twórcy": g.Tworcy,
            "Wydawca": g.Wydawca,
            "Dostępna": g.Dostepna,
            "Multiplayer": g.Multiplayer,
            "Coop": g.Coop,
        })
    return O