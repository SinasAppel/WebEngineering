from django.urls import path, register_converter

from . import views, converters


register_converter(converters.CarrierCodeConverter, 'ccode')

urlpatterns = [
    path('', views.index, name='index'),
    path('statistics/<ccode:carrier_code>/flights', views.flights, name='flights'),
    path('statistics/<ccode:carrier_code>/flights/delays', views.delays, name='delays'),
    path('statistics/<ccode:carrier_code>/delay-minutes', views.minutes, name='minutes'),
    path('time', views.time, name='time')
]
