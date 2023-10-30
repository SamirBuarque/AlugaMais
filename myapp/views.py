from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return HttpResponse('Home')

def test(request):
    return HttpResponse('pagina teste')

def contato(request):
    return HttpResponse('pagina contato')