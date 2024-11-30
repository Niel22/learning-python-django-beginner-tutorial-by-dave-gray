# from django.http import HttpResponse
from django.shortcuts import render

def homePage(request):
    # return HttpResponse("Hello world! i'm home")
    return render(request, 'home.html')

def about(request):
    # return HttpResponse("My About Page")
    return render(request, 'about.html')