# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request,"index.html",{})


def machine_booking_view(request):
    return render(request,"machine.html",{})


def consumables_view(request):
    return render(request,"consumables.html",{})