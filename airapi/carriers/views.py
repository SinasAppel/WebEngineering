from django.http import HttpResponse
from .models import Carrier


def index(request):
    airport_code = request.GET.get('airport-code', False)
    if airport_code:
        return HttpResponse(airport_code)
    else:
        carrier_list = Carrier.objects.order_by('code')
        output = []
        for a in carrier_list:
            if a.toJSON() not in output:
                output.append(a.toJSON())
        return HttpResponse(output)
