from django.http import HttpResponse

from .models import Airport


def index(request):
    airport_list = Airport.objects.order_by('code')
    output = ', '.join([a.toJSON() for a in airport_list])
    return HttpResponse(output)
