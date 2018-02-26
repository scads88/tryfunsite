from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("sup girls")
# Create your views here.
