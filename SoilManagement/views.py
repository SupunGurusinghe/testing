from django.shortcuts import render
from django.http import HttpResponse


def soil(request):
    return render(request, 'Soil.html')


def index(request):
    return render(request, 'Soil.html')


def searchplant(request):
    return render(request, 'Search-Plant.html')


def searchtest(request):
    return render(request, 'Search-Test.html')


def fertilizerchecking(request):
    return render(request, 'Fertilizer-Checking.html')


def addplant(request):
    return render(request, 'Add-Plant.html')
