from django.contrib import admin
from django.urls import include, path

from . import views

urlpatterns = [
    path("",views.a_propos_page, name="a_propos")
]