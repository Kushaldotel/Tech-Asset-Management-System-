from django.urls import path
from device_detection.views import device_detection_view
from django.shortcuts import redirect

urlpatterns = [
    path('', lambda request: redirect('/device-detection/')), # this to go to the admin link directly
    path('device-detection/', device_detection_view, name='device_detection'),
]
