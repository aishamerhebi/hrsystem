from django.shortcuts import render
from django.http import HttpResponse

def employees(request):
    return HttpResponse("Hello world!")