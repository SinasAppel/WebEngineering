from django.http import HttpResponse
from .models import Carrier


def index(request):
    airport_code = request.GET.get('airport-code', False)
    if airport_code:
        return HttpResponse(airport_code)
    else:
        airport_list = Carrier.objects.order_by('code')
        output = ', '.join([a.toJSON() for a in airport_list])
        return HttpResponse(output)
