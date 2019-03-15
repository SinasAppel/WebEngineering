from django.http import HttpResponse


def index(request):
    output = "Carrier"
    return HttpResponse(output)