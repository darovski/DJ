from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request, 'main/index.html', {'caption':"Django"})

def new(request):
    return render(request, 'main/new.html', {'caption': "Django"})

def data(request):
    return render(request, 'main/page3.html', {'caption': "Django"})

def test(request):
    return render(request, 'main/page4.html', {'caption': "Django"})