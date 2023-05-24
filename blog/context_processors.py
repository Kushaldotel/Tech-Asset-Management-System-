# myapp/context_processors.py
from django.shortcuts import get_object_or_404
from .models import *

def global_context(request):
    # Define the variables you want to include in the global context
    asset = get_object_or_404(Asset, id=1)
    dashboard = asset.dashboard_value  # Assign the value of hardware to dashboard
    software = asset.software_value
    enable_dashboard = True if dashboard else False
    enable_software = True if software else False
    global_variables = {
        'my_variable': 'Hello, world!',
        'another_variable': 42,
        'enable_dashboard': enable_dashboard,
        'enable_software': enable_software,
    }
    return global_variables

