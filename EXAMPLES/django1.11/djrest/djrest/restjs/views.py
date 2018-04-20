from django.shortcuts import render

# Create your views here.

# example:
def home(request):
    return render(request, 'home.html')
