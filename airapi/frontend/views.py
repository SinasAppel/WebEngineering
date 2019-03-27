from django.shortcuts import render
import requests
import json
from airports.models import Airport
from carriers.models import  Carrier

def index(request):
    context = {
        'active': "Home",
    }
    return render(request, 'frontend/index.html', context)


def airports(request):
    r = requests.get('http://localhost:8000/v1/airports')
    airport_json = json.loads(r.json())
    for a in airport_json:
        print(a)
        print(a['airport'])

    context = {
        'airport_list': airport_json,
        'active': "Airports",
    }
    return render(request, 'frontend/airports.html', context)


def carriers(request):
    r = requests.get('http://localhost:8000/v1/carriers')
    carrier_json = json.loads(r.json())
    for c in carrier_json:
        print(c)
        print(c['carrier'])

    context = {
        'carrier_list': carrier_json,
        'active': "Carriers",
    }
    return render(request, 'frontend/carriers.html', context)


def carriers_at_airport(request):
    context = {
        'active': "Carriers at Airport",
    }
    return render(request, 'frontend/carriers_at_airport.html', context)


def carrier_statistics(request):
    context = {
        'active': "Carrier Statistics",
    }
    return render(request, 'frontend/carrier_statistics.html', context)


def carrier_delays(request):
    context = {
        'active': "Number of Carrier Delays",
    }
    return render(request, 'frontend/number_of_carrier_delays.html', context)


def carrier_delays_minutes(request):
    context = {
        'active': "Minutes of Carrier Delays",
    }
    return render(request, 'frontend/minutes_of_carrier_delays.html', context)


def carrier_delays_statistics(request):
    context = {
        'active': "Statistics of Carrier Delays",
    }
    return render(request, 'frontend/statistics_of_carrier_delays.html', context)
