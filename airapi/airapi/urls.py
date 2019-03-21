from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('v1/airports/', include('airports.urls')),
    path('v1/carriers/', include('carriers.urls')),
    path('admin/', admin.site.urls),
]