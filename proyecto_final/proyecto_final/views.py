from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request, 'index.html', context={})

#def clothes (request):
    #return render(request, 'clothes.html')

#def sales (request):
    #return render(request, 'sales.html')
