from django.http import HttpResponse
from django.http import JsonResponse
import json

from airports.models import Airport
from .models import Carrier


def index(request):
    airport_code = request.GET.get('airport-code', False)
    unique_carriers = []
    carrier_set = []
    carrier_list = Carrier.objects.order_by()

    # Depending on if the get request data contains an airport code (/v1/carriers?airport_code=)
    # create a carrier_list of carriers that should be returned
    if airport_code:
        airport_list = Airport.objects.order_by()
        i = 0
        for airport in airport_list:
            if airport_code == airport.get_code():
                if carrier_list[i].to_json() not in unique_carriers:
                    unique_carriers.append(carrier_list[i].to_json())
                    carrier_set.append(carrier_list[i])
            i = i + 1
    else:
        for a in carrier_list:
            if a.to_json() not in unique_carriers:
                unique_carriers.append(a.to_json())
                carrier_set.append(a)

    if carrier_set is []:
        return HttpResponse(content="Error 503: List of carriers cannot be found.", status=503)

    return JsonResponse(json.dumps([carrier.dump() for carrier in carrier_set]), safe=False, status=200)


def flights(request, carrier_code):
    return HttpResponse(carrier_code)
