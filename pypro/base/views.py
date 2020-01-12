# -*- coding: utf-8 -*-
from django.shortcuts import render  # noqa

# Create your views here.
from pypro.modulos import facade


def home(request):
    return render(request, 'base/home.html', {'MODULOS': facade.listar_modulos_ordenados()})
