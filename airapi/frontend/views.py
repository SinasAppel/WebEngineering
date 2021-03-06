from django.shortcuts import render
from django.http import HttpResponse
import requests
import json

def index(request):
    context = {
        'active': "Home",
    }
    return render(request, 'frontend/index.html', context)


def airports(request):
    r = requests.get('http://localhost:8000/v1/airports')
    airport_json = json.loads(r.json())

    context = {
        'airport_list': airport_json,
        'active': "Airports",
    }
    return render(request, 'frontend/airports.html', context)


def carriers(request):
    r = requests.get('http://localhost:8000/v1/carriers')
    carrier_json = json.loads(r.json())

    context = {
        'carrier_list': carrier_json,
        'active': "Carriers",
    }

    return render(request, 'frontend/carriers.html', context)


def carriers_at_airport(request):
    context = {
        'active': "Carriers at Airport",
    }

    if request.method == 'POST':
        airport_code = request.POST.get("airport_code", False)
        if not airport_code:
            return HttpResponse('Error 400: Failed to give airport code', status=400)
        rs = "http://localhost:8000/v1/carriers"
        rs = rs + "?airport-code=" + airport_code
        r = requests.get(rs)
        j = json.loads(r.json())
        context['data'] = j

    return render(request, 'frontend/carriers_at_airport.html', context)


def carrier_statistics(request):
    context = {
        'active': "Carrier Statistics",
    }

    if request.method == 'POST':
        print("Post method detected")
        carrier_code = request.POST.get("carrier_code", False)
        if not carrier_code:
            return HttpResponse('Error 400: Failed to give carrier code', status=400)
        airport_code = request.POST.get("airport_code", False)
        if not airport_code:
            return HttpResponse('Error 400: Failed to give airport code', status=400)
        month = request.POST.get("month", False)
        year = request.POST.get("year", False)
        rs = "http://localhost:8000/v1/carriers/statistics/"
        rs = rs + carrier_code + "/flights"
        rs = rs + "?airport-code=" + airport_code
        if year and month:
            rs = rs + "&year=" + year + "&month=" + month
        r = requests.get(rs)
        j = json.loads(r.json())
        on_time = []
        for i in range(len(j)):
            on_time.append(j[i]['flights']['on time'])
        context['data'] = zip(j, on_time)

    return render(request, 'frontend/carrier_statistics.html', context)


def carrier_delays(request):
    context = {
        'active': "Number of Carrier Delays",
    }
    if request.method == 'POST':
        carrier_code = request.POST.get("carrier_code", False)
        if not carrier_code:
            return HttpResponse('Error 400: Failed to give carrier code', status=400)
        airport_code = request.POST.get("airport_code", False)
        if not airport_code:
            return HttpResponse('Error 400: Failed to give airport code', status=400)
        month = request.POST.get("month", False)
        year = request.POST.get("year", False)
        rs = "http://localhost:8000/v1/carriers/statistics/"
        rs = rs + carrier_code + "/flights/delays"
        rs = rs + "?airport-code=" + airport_code
        if year and month:
            rs = rs + "&year=" + year + "&month=" + month
        r = requests.get(rs)
        j = json.loads(r.json())
        len_j = len(j)
        late_aircraft = []
        weather = []
        security = []
        national_aviation_system = []
        carrier = []
        for i in range(len_j):
            late_aircraft.append(j[i]['delays']['late aircraft'])
            weather.append(j[i]['delays']['weather'])
            security.append(j[i]['delays']['security'])
            national_aviation_system.append(j[i]['delays']['security'])
            carrier.append(j[i]['delays']['carrier'])
        data = zip(late_aircraft, weather, security, national_aviation_system, carrier)
        context['data'] = data

    return render(request, 'frontend/number_of_carrier_delays.html', context)


def carrier_delays_minutes(request):
    context = {
        'active': "Minutes of Carrier Delays",
    }
    if request.method == 'POST':
        carrier_code = request.POST.get("carrier_code", False)
        if not carrier_code:
            return HttpResponse('Error 400: Failed to give carrier code', status=400)
        airport_code = request.POST.get("airport_code", False)
        if not airport_code:
            return HttpResponse('Error 400: Failed to give airport code', status=400)
        reason = request.POST.get("reason", False)
        month = request.POST.get("month", False)
        year = request.POST.get("year", False)
        rs = "http://localhost:8000/v1/carriers/statistics/"
        rs = rs + carrier_code + "/delay-minutes"
        rs = rs + "?airport-code=" + airport_code
        if reason:
            rs = rs + "&reason=" + reason
        if month and year:
            rs = rs + "&month=" + month
            rs = rs + "&year=" + year
        r = requests.get(rs)
        j = json.loads(r.json())
        if reason:
            data_with_reason = j
            context['data_with_reason'] = data_with_reason
            context['reason'] = reason
        else:
            len_j = len(j)
            late_aircraft = []
            weather = []
            security = []
            national_aviation_system = []
            carrier = []
            month = []
            year = []
            for i in range(len_j):
                late_aircraft.append(j[i]['delays']['late aircraft'])
                weather.append(j[i]['delays']['weather'])
                security.append(j[i]['delays']['security'])
                national_aviation_system.append(j[i]['delays']['security'])
                carrier.append(j[i]['delays']['carrier'])
                month.append(j[i]['time']['month'])
                year.append(j[i]['time']['month'])
            data = zip(month, year, late_aircraft, weather, security, national_aviation_system, carrier)
            context['data'] = data
    return render(request, 'frontend/minutes_of_carrier_delays.html', context)


def carrier_delays_statistics(request):
    context = {
        'active': "Statistics of Carrier Delays",
    }

    if request.method == 'POST':
        airport_a = request.POST.get("airport_a", False)
        if not airport_a:
            return HttpResponse('Error 400: Failed to give airport code', status=400)
        airport_b = request.POST.get("airport_b", False)
        if not airport_b:
            return HttpResponse('Error 400: Failed to give airport code', status=400)
        carrier_code = request.POST.get("carrier_code", False)
        if not carrier_code:
            return HttpResponse('Error 400: Failed to give carrier code', status=400)
        rs = "http://localhost:8000/v1/airports/statistics/descriptive"
        rs = rs + "?airport-a=" + airport_a
        rs = rs + "&airport-b=" + airport_b
        rs = rs + "&carrier-code=" + carrier_code
        r = requests.get(rs)
        j = json.loads(r.json())
        print(json.dumps(j))
        airport_a = []
        airport_b = []
        carrier_code = []
        mean = []
        median = []
        standard_deviation = []
        airport_a.append(j['airport-a'])
        airport_b.append(j['airport-b'])
        carrier_code.append(j['carrier-code'])
        mean.append(j['stats']['mean'])
        median.append(j['stats']['median'])
        standard_deviation.append(j['stats']['standard-deviation'])
        data = zip(airport_a, airport_b, carrier_code, mean, median, standard_deviation)
        context['data'] = data

    return render(request, 'frontend/statistics_of_carrier_delays.html', context)
