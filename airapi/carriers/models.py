import json
from django.db import models

from airports.models import Airport


class Carrier(models.Model):
    code = models.CharField(max_length=3)
    name = models.CharField(max_length=200)

    def dump(self):
        return {"carrier": {'code': self.code,
                            'name': self.name}}

    def to_json(self):
        data = {'name': self.name, 'code': self.code}
        return json.dumps(data)


class Flights(models.Model):
    cancelled = models.IntegerField()
    on_time = models.IntegerField()
    total = models.IntegerField()
    delayed = models.IntegerField()
    diverted = models.IntegerField()


class Delays(models.Model):
    late_aircraft = models.IntegerField()
    weather = models.IntegerField()
    security = models.IntegerField()
    national_aviation_system = models.IntegerField()
    carrier = models.IntegerField()


class MinutesDelayed(models.Model):
    late_aircraft = models.IntegerField()
    weather = models.IntegerField()
    carrier = models.IntegerField()
    security = models.IntegerField()
    total = models.IntegerField()
    national_aviation_system = models.IntegerField()


class Statistics(models.Model):
    flights = models.ForeignKey(Flights, on_delete=models.CASCADE)
    delays = models.ForeignKey(Delays, on_delete=models.CASCADE)
    minutes_delayed = models.ForeignKey(MinutesDelayed, on_delete=models.CASCADE)


class Time(models.Model):
    label = models.CharField(max_length=20)
    year = models.IntegerField()
    month = models.IntegerField()


class CarrierData(models.Model):
    carrier = models.ForeignKey(Carrier, on_delete=models.CASCADE)
    airport = models.ForeignKey(Airport, on_delete=models.CASCADE)
    statistics = models.ForeignKey(Statistics, on_delete=models.CASCADE)
    time = models.ForeignKey(Time, on_delete=models.CASCADE)
