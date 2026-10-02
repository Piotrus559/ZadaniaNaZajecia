from django.shortcuts import render
from django.http import HttpResponse
import datetime

def hello(request):
    return HttpResponse("Witaj w Django!")

def hello_name(request, name):
    return HttpResponse(f"Witaj, {name}!")

def hello_template(request, name):
    return render(request, "witaj/hello.html", {"name": name})

def time(request):
    Czas = datetime.datetime.now()
    return render(request, "witaj/time.html", {"data": datetime.date.today(), "czas": Czas.time().isoformat("seconds")})