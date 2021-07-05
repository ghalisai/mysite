from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, world. You're at the sai.")


def message(request):
    return HttpResponse("<h1> hi Sai </h1>")
