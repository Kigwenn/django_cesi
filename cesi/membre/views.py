from django.shortcuts import render
from django.template import Context, loader
from membre.models import Membre
from django.http import HttpResponse

# Create your views here.
def index(request):
    membre_list = Membre.object.all()

    return render(request, "membre.html", {'membre_list': membre_list})

def add(request):
    membre_list = Membre.object.all()

    return render(request, "membreAdd.html")

def modify(request):
    membre_list = Membre.object.all()

    return render(request, "membreModify.html")