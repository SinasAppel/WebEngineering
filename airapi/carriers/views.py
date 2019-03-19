from django.http import HttpResponse
from django.http import JsonResponse
import json
from .models import Carrier
from .models import CarrierData


def index(request):
    airport_code = request.GET.get('airport-code', False)
    carrier_list = []

    # Depending on if the get request data contains an airport code (/v1/carriers?airport_code=)
    # create a carrier_list of carriers that should be returned
    if airport_code:
        carrier_data = CarrierData.objects.order_by('carrier__code')
        for cd in carrier_data:
            if airport_code == cd.get_airport().get_code():
                carrier_list.append(cd.get_carrier())
    else:
        carrier_list = Carrier.objects.order_by('code')

    if carrier_list is []:
        return HttpResponse(content="Error 503: List of carriers cannot be found.", status=503)
    unique_carriers = []
    carrier_set = []
    for a in carrier_list:
        if a.to_json() not in unique_carriers:
            unique_carriers.append(a.to_json())
            carrier_set.append(a)
    return JsonResponse(json.dumps([carrier.dump() for carrier in carrier_set]), safe=False, status=200)
