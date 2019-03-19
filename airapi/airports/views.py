from django.http import JsonResponse
from django.http import HttpResponse
import json
from .models import Airport


def index(request):
    airport_list = Airport.objects.order_by('code')
    if airport_list is []:
        return HttpResponse(content="Error 503: List of airports cannot be found.", status=503)
    unique_airports = []
    airport_set = []
    for a in airport_list:
        if a.to_json() not in unique_airports:
            unique_airports.append(a.to_json())
            airport_set.append(a)

    return JsonResponse(json.dumps([airport.dump() for airport in airport_set]), safe=False, status=200)


def statistics(request):
    output = "Hello"
    return HttpResponse(output)
