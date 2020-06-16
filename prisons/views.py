from django.http import HttpResponse
from django.shortcuts import render
from .models import Prison

def search(request):
    return HttpResponse("Hello, world")

def prison(request, prison_pk, name):
    p = Prison.objects.get(pk=prison_pk)
    return render(request, 'prisons/prisonDetail.html', {'prison': p})