from django.shortcuts import render , get_object_or_404, redirect
from .models import Tracker
import requests

# Create your views here.

def home(request):
    link = requests.get('https://corona.lmao.ninja/v2/all')
    link1 = requests.get('https://corona.lmao.ninja/v2/countries/BD')
    link2 = requests.get('https://disease.sh/v2/countries/Bangladesh?yesterday=true&strict=true')
    link1 = link1.json()
    link = link.json()
    link2 = link2.json()
    print(link1)
    print(link2)
    return render(request, 'deshboard.html', {
        'globaldata':link,
        'bangladesh':link1,
        'bdyes':link2
    })
