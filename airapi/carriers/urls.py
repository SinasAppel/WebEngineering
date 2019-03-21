from django.urls import path, register_converter

from . import views, converters


register_converter(converters.CarrierCodeConverter, 'ccode')
register_converter(converters.AirportCodeConverter, 'acode')


urlpatterns = [
    path('', views.index, name='index'),
    path('statistics/<ccode:code>/flights/<acode:airport>/<int:month>/', views.statistics, name='statistics'),
    path('statistics/<ccode:code>/flights/delays/<acode:airport>/<int:month>', views.delays, name='delays'),
    path('time', views.time, name='time')
]
