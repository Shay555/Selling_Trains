# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
def get_index(request):
    return render(request, 'index.html')

def get_home(request):
    return render(request, 'index.html')

def get_Contact(request):
   return render(request, 'contact.html')

def get_Privacy(request):
   return render(request, 'selling-policy.html')

def get_Sell(request):
   return render(request, 'Sell.html')

def get_Buy(request):
   return render(request,'Buy.html')