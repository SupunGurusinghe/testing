from django.http import HttpResponse
from django.shortcuts import render


def carts(request):
	context={}
	return render(request,'cart.html',context)


def checkout(request):
	context={}
	return render(request,'checkout.html',context)


def store(request):
	context={}
	return render(request,'store.html',context)

