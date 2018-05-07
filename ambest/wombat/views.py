from django.shortcuts import render
from django.http.response import HttpResponse
# Create your views here.

def index(request):
    return HttpResponse("Welcome to A. M. Best Web App")


# https://github.com/jstrickler/ambest
