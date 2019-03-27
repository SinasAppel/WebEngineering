from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('airports', views.airports, name='airports'),
    path('carriers', views.carriers, name='carriers'),
    path('carriers/at-airport', views.carriers_at_airport, name='carriers_at_airport'),
    path('carriers/statistics', views.carrier_statistics, name='carrier_statistics'),
    path('carriers/delays', views.carrier_delays, name='carrier_delays'),
    path('carriers/delays/minutes', views.carrier_delays_minutes, name='carrier_delays_minutes'),
    path('carriers/delays/statistics', views.carrier_delays_statistics, name='carrier_delays_statistics'),
]
