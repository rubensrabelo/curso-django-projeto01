from django.http import HttpResponse
from django.shortcuts import render


def home(request):
    return render(request, 'global/home.html')


def sobre(request):
    return HttpResponse('SOBRE 1')


def contato(request):
    return HttpResponse('CONTATO 1')
