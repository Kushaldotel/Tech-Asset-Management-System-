
from django.shortcuts import render

def device_detection_view(request):
    return render(request, 'device_detection.html')
