from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")


def message(request):
    return HttpResponse("<h1> hi Sai </h1>")
