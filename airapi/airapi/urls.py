from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('airports/', include('airports.urls')),
    path('admin/', admin.site.urls),
]