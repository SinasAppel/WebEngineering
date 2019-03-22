from django.db.models import Q
from django.http import JsonResponse
from django.http import HttpResponse
import json
import statistics


from carriers.models import Carrier, MinutesDelayed, CarrierData, Statistics
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


def statistics_view(request):
    class Stats:
        def __init__(self, m, med, s, a, b, c):
            self.mean = m
            self.median = med
            self.std = s
            self.airport_a = a
            self.airport_b = b
            self.carrier_code = c

        def dump(self):
            return {"airport-a": self.airport_a,
                    "airport-b": self.airport_b,
                    "carrier-code": self.carrier_code,
                    "stats": {'mean': self.mean,
                              'median': self.median,
                              'standard-deviation': self.std}
                    }

    airport_a = request.GET.get('airport-a', False)
    airport_b = request.GET.get('airport-b', False)
    carrier_code = request.GET.get('carrier-code', False)

    if not airport_a or not airport_b:
        return HttpResponse("400: airport code of at least 2 airports is required", status=400)

    airport_list = Airport.objects.all().values_list('code')
    carrier_list = Carrier.objects.all().values_list('code')
    delays = MinutesDelayed.objects.order_by()
    l = len(carrier_list)
    if carrier_code:
        indexes = []
        for i in range(l):
            if carrier_list[i][0] == carrier_code:
                if airport_list[i][0] == airport_a or airport_list[i][0] == airport_b:
                    indexes.append(i)
        # Check if a carrier is on both airports
        airport_a_present = False
        airport_b_present = False
        for i in indexes:
            if airport_list[i][0] == airport_a:
                airport_a_present = True
            if airport_list[i][0] == airport_b:
                airport_b_present = True

        if airport_a_present and airport_b_present:
            delays_filtered = []
            for i in indexes:
                delays_filtered.append((delays[i].get_carrier() + delays[i].get_late_aircraft()))
            stats = Stats(statistics.mean(delays_filtered), statistics.median(delays_filtered), statistics.stdev(delays_filtered), airport_a, airport_b, carrier_code)
            return JsonResponse(json.dumps(stats.dump()), safe=False, status=200)
        else:
            return HttpResponse("Error 404: the given airline does not fly on one or both of the given airports", status=404)
    else:
        # The following codeblock technically works but takes way too long of a time to be realistic for implementation
        # (multiple minutes to finish a request)
        # Hence the not implemented error
        return HttpResponse("Error 400: Missing carrier-code", status=400)
        # indexes = []
        # for i in range(l):
        #     if airport_list[i][0] == airport_a or airport_list[i][0] == airport_b:
        #         indexes.append(i)
        # unique_carriers = []
        # indexes_len = len(indexes)
        # for i in range(indexes_len):
        #     if carrier_list[i][0] not in unique_carriers:
        #         unique_carriers.append(carrier_list[i][0])
        # carriers_on_both_airports = []
        # for c in unique_carriers:
        #     # Check if a carrier is on both airports
        #     airport_a_present = False
        #     airport_b_present = False
        #     for i in indexes:
        #         cc = carrier_list[i][0]
        #         ac = airport_list[i][0]
        #         if cc == c and ac == airport_a:
        #             airport_a_present = True
        #         if cc == c and ac == airport_b:
        #             airport_b_present = True
        #     if airport_a_present and airport_b_present:
        #         carriers_on_both_airports.append(c)
        # stats = []
        # for c in carriers_on_both_airports:
        #     delays_filtered = []
        #     for i in indexes:
        #         if carrier_list[i].get_code() == c:
        #             delays_filtered.append(delays[i].get_carrier() + delays[i].get_late_aircraft())
        #     s = Stats(statistics.mean(delays_filtered), statistics.median(delays_filtered), statistics.stdev(delays_filtered), airport_a, airport_b, c)
        #     stats.append(s)
        # return JsonResponse(json.dumps([s.dump() for s in stats]), status=200)
