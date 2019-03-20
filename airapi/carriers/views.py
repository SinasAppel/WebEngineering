from django.http import HttpResponse
from django.http import JsonResponse
import json

from airports.models import Airport
from .models import Carrier, Flights, Time


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
    class Stats:
        def __init__(self, f, a, c, t):
            self.flights = f
            self.airport = a
            self.carrier = c
            self.time = t

        def dump(self):
            return {"flights": {'cancelled': self.flights.get_cancelled(),
                                'on time': self.flights.get_on_time(),
                                'total': self.flights.get_total(),
                                'delayed': self.flights.get_delayed(),
                                'diverted': self.flights.get_diverted()},
                    "airport": {'code': self.airport.get_code(),
                                'name': self.airport.get_name()},
                    "carrier": {'code': self.carrier.get_code(),
                                'name': self.carrier.get_name()},
                    "time": {'label': self.time.get_label(),
                             'year': self.time.get_year(),
                             'month': self.time.get_month()}
                    }

    airport_code = request.GET.get('airport-code', False)
    month = int(request.GET.get('month', False))
    year = int(request.GET.get('year', False))
    if not airport_code:
        return HttpResponse("Error, no airport-code given", status=400)

    stat_list = []
    flight_list = Flights.objects.order_by()
    airports = Airport.objects.order_by()
    carriers = Carrier.objects.order_by()
    time = Time.objects.order_by()
    if not month or not year:
        for i in range(1000):
            if carriers[i].get_code() == carrier_code and airports[i].get_code() == airport_code:
                s = Stats(flight_list[i], airports[i], carriers[i], time[i])
                stat_list.append(s)
    else:
        for i in range(1000):
            if carriers[i].get_code() == carrier_code and airports[i].get_code() == airport_code:
                if month == time[i].get_month() and year == time[i].get_year():
                    s = Stats(flight_list[i], airports[i], carriers[i], time[i])
                    stat_list.append(s)

    return JsonResponse(json.dumps([s.dump() for s in stat_list]), safe=False)
