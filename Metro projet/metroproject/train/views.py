from django.shortcuts import render, redirect #a changer
from django.http import HttpResponse
from .models import wagon
import random

# Create your views here.

def index(request):
    mes_id_wagon = request.GET['recherche'] if 'recherche' in request.GET else None
    return redirect('detail', id_wagon=mes_id_wagon) if 'recherche' in request.GET else render(request, "train/index.html", {"all_wagon": wagon.objects.all(), "random": random.randint(1, 15)})

def detail(request, id_wagon) :
    list_wagon = wagon.objects.get(id = id_wagon)
    wagon_un = list_wagon

    return render(request, "train/detail.html", {
        "id" : wagon_un.id,
        "horaire_plan" : wagon_un.horaire_plan,
        "voyage" : wagon_un.voyage,
        "img" : wagon_un.img,
        "nextID" : int(id_wagon) + 1,
        
    })


