from django.shortcuts import render , get_object_or_404, redirect
from .models import Tracker
import requests

# Create your views here.

def home(request):
    link = requests.get('https://corona.lmao.ninja/v2/all')
    link = link.json()
    print(link)
    return render(request, 'deshboard.html', {
        'globaldata':link
    })
