from django.shortcuts import render
from django.template import Context, loader
from promotion.models import Promotion
from django.http import HttpResponse

# Create your views here.
def index(request):
    promotion_list = Promotion.object.all()

    return render(request, "promotion.html", {'promotion_list': promotion_list})