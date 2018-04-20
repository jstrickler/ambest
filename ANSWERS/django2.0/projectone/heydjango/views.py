from django.http import HttpResponse

def home(request):
    return HttpResponse("I am now a Django developer!")

