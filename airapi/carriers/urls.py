from django.urls import path, register_converter

from . import views, converters


register_converter(converters.CarrierCodeConverter, 'ccode')
register_converter(converters.AirportCodeConverter, 'acode')


urlpatterns = [
    path('', views.index, name='index'),
    path('<str:return_type>', views.index, name='index'),
    path('statistics/<ccode:code>/flights/<acode:airport>/<int:month>', views.statistics, name='statistics'),
    path('statistics/<ccode:code>/flights/<acode:airport>/<int:month>/<str:return_type>', views.statistics, name='statistics'),
    path('statistics/<ccode:code>/flights/delays/<acode:airport>/<int:month>', views.delays, name='delays'),
    path('statistics/<ccode:code>/flights/delays/<acode:airport>/<int:month>/<str:return_type>', views.delays, name='delays'),
    path('statistics/<ccode:code>/delay-minutes/<str:reason>/<acode:airport>/<int:month>', views.minutes, name='minutes'),
    path('statistics/<ccode:code>/delay-minutes/<str:reason>/<acode:airport>/<int:month>/<str:return_type>', views.minutes, name='minutes'),
    path('statistics/descriptive/<acode:airport_a>/<acode:airport_b>', views.descriptive, name='descriptive'),
    path('statistics/descriptive/<acode:airport_a>/<acode:airport_b>/<str:return>', views.descriptive, name='descriptive'),
    path('time', views.time, name='time')
]
