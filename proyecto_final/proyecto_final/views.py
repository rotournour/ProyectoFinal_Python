from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request, 'index.html', context={})

def testimony (request):
    return HttpResponse ('Aca van los testimonios')

def recommendation (request):
    return HttpResponse ('Recomendacion de usuarios')
