from django.shortcuts import render
from django.template import Context, loader
from blog.models import Publication
from django.http import HttpResponse

# Create your views here.
def index(request):
    publication_list = Publication.object.all()

    return render(request, "index.html", {'publication_list': publication_list})