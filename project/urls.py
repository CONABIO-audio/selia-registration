from django.conf.urls import url
from django.conf.urls import include


urlpatterns = [
    url(
        r'^registration/',
        include('selia_registration.urls')),
]
