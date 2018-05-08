from django.shortcuts import render
from django.http.response import HttpResponse
from . import models

# Create your views here.

# example:
# def home(request):
#     context = { 'message': 'Hello' }
#     return render(request, 'ambfun/home.html', context)


def index(request):
    return HttpResponse("Another Fine Web App")

def toast(request):
    a_toast = models.Toast.objects.filter(bread_type='sourdough').first()
    context = {'toast': a_toast, 'all_toast': models.Toast.objects.all()}
    return render(request, 'ambfun/toast.html', context)
