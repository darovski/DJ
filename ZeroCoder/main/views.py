from django.http import HttpResponse

def index(request):
    return HttpResponse("<h1>Это главная страница проекта</h1>")

def new(request):
    return HttpResponse("<h1>Это вторая страница проекта</h1>")

def data(request):
    return HttpResponse("<h1>Это еще одна страница проекта</h1>")

def test(request):
    return HttpResponse("<h1>не думал, что дойдете до этой страницы</h1>")