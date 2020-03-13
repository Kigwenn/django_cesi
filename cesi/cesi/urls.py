"""cesi URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('publication/', include('publication.urls'))
"""
from . import settings
from django.contrib import admin
from django.urls import path
from django.conf.urls import url
from django.contrib.staticfiles.urls import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from publication import views as puviews
from promotion import views as pviews
from membre import views as mviews
from typeMembre import views as tmviews
# from trombinoscope import views as tviews

urlpatterns = [
    path('admin/', admin.site.urls),
    path('/', admin.site.urls),

    url('promotion/add/', pviews.add, name="promotionAdd"),
    url('promotion/modify/', pviews.modify, name="promotionModify"),
    url('promotion/', pviews.index, name="promotion"),

    url('membre/add/', mviews.add, name="membreAdd"),
    url('membre/modify/', mviews.modify, name="membreModify"),
    url('membre/', mviews.index, name="membre"),
    url('membreTrombi', mviews.trombi, name="membreTrombi"),
    url('index', mviews.home, name="index"),


    url('typeMembre/add/', tmviews.add, name="typeMembreAdd"),
    url('typeMembre/modify/', tmviews.modify, name="typeMembreModify"),
    url('typeMembre/', tmviews.index, name="typeMembre"),

    url('publication/add/', puviews.add, name="publicationAdd"),
    url('publication/modify/', puviews.modify, name="publicationModify"),
    url('publication/', puviews.index, name="publication"),

    # url('trombinoscope/add/', tviews.add, name="trombinoscopeAdd"),
    # url('trombinoscope/modify/', tviews.modify, name="trombinoscopeModify"),
    # url('trombinoscope/', tviews.index, name="trombinoscope"),
]

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)