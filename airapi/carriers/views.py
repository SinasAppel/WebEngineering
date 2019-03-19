from django.http import HttpResponse
from django.http import JsonResponse
import json
from .models import Carrier


def index(request):
    airport_code = request.GET.get('airport-code', False)
    if airport_code:
        return HttpResponse(airport_code)
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

        return JsonResponse(json.dumps([airport.dump() for airport in carrier_set]), safe=False, status=200)
