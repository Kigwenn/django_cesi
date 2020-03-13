from django.shortcuts import render
from django.template import Context, loader
from membre.models import Membre
from django.http import HttpResponse

# Create your views here.
def index(request):
    membre_list = Membre.object.all()

    return render(request, "membre.html", {'membre_list': membre_list})

def add(request):

    if request.method == 'POST':
        membre = Membre()
        membre.nom = request.POST.get("nom")
        membre.prenom = request.POST.get("prenom")
        membre.adresse = request.POST.get("adresse")
        membre.cp = request.POST.get("cp")
        membre.tel = request.POST.get("code_postal")
        membre.date_naissance = request.POST.get("date_naissance_0")
        membre.date_entre = request.POST.get("date_entre_0")
        membre.date_sortie = request.POST.get("date_sortie_0")
        membre.save()

        membre_list = Membre.object.all()
        return render(request, "membre.html", {'membre_list': membre_list})
    else:
        return render(request, "membreAdd.html")

def modify(request):
    membre_id = request.GET.get('id')[0]
    membre = Membre.object.all()
    print(membre)
    request("nom") = membre.nom
    membre.prenom = request.set("prenom")
    membre.adresse = request.POST.get("adresse")
    membre.cp = request.POST.get("cp")
    membre.tel = request.POST.get("code_postal")
    membre.date_naissance = request.POST.get("date_naissance_0")
    membre.date_entre = request.POST.get("date_entre_0")
    membre.date_sortie = request.POST.get("date_sortie_0")

    if request.method == 'PUT':
        membre.nom = request.POST.get("nom")
        membre.prenom = request.POST.get("prenom")
        membre.adresse = request.POST.get("adresse")
        membre.cp = request.POST.get("cp")
        membre.tel = request.POST.get("code_postal")
        membre.date_naissance = request.POST.get("date_naissance_0")
        membre.date_entre = request.POST.get("date_entre_0")
        membre.date_sortie = request.POST.get("date_sortie_0")
        membre.save()

        membre_list = Membre.object.all()
        return render(request, "membre.html", {'membre_list': membre_list})
    else:
        return render(request, "membreModify.html")

def delete(request):
    if request.method == 'delete':
        membre_id = request.GET.get('id')[0]
        Membre.object.find(id=membre_id).delete()

        membre_list = Membre.object.all()
        return render(request, "membre.html", {'membre_list': membre_list})
    else:
        return render(request, "membreModify.html")
