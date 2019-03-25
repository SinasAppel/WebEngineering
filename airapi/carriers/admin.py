from django.contrib import admin

from .models import Carrier
from .models import CarrierData

admin.site.register(Carrier)
admin.site.register(CarrierData)