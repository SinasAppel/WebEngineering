from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('statistics/descriptive', views.statistics, name='statistics')
]