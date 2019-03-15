from django.http import HttpResponse
from .models import Airport


def index(request):
    airport_list = Airport.objects.order_by('code')
    output = []
    for a in airport_list:
        if a.toJSON() not in output:
            output.append(a.toJSON())
    return HttpResponse(output)


def statistics(request):
    output = "Hello"
    return HttpResponse(output)
