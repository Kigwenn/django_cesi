from django.shortcuts import render
from django.template import Context, loader
from membre.models import Membre
from django.http import HttpResponse

# Create your views here.
def index(request):

    if request.method=='GET':
        promo_id = request.GET.get('promo_id')

        if not promo_id:
            membre_list = Membre.object.all()
            return render(request, "membre.html", {'membre_list': membre_list})
        else:
            # now you have the value of sku
            # so you can continue with the rest
            membre_list = Membre.object.filter(promotion=promo_id)
            return render(request, "membre.html", {'membre_list': membre_list})




def add(request):
    membre_list = Membre.object.all()

    return render(request, "membreAdd.html")

def modify(request):
    membre_list = Membre.object.all()

    return render(request, "membreModify.html")

def trombi(request):
    if request.method=='GET':
        promo_id = request.GET.get('promo_id')

        if not promo_id:
            membre_list = Membre.object.all()
            return render(request, "trombinoscope.html", {'membre_list': membre_list})
        else:
            # now you have the value of sku
            # so you can continue with the rest
            membre_list = Membre.object.filter(promotion=promo_id)
            return render(request, "trombinoscope.html", {'membre_list': membre_list})

def home(request):

    return render(request, "index.html")
