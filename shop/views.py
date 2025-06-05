from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return render(request, 'shop/index.html')


def about(request):
    return HttpResponse('about us')


def tracker(request):
    return HttpResponse('tracker')


def contact(request):
    return HttpResponse('contact')


def prodView(request):
    return HttpResponse('prodView')


def checkout(request):
    return HttpResponse('checkout')


def search(request):
    return HttpResponse('search')
