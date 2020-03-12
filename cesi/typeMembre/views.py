from django.shortcuts import render
from django.template import Context, loader
from typeMembre.models import TypeMembre
from django.http import HttpResponse

# Create your views here.
def index(request):
    typeMembre_list = TypeMembre.object.all()

    return render(request, "typeMembre.html", {'typeMembre_list': typeMembre_list})