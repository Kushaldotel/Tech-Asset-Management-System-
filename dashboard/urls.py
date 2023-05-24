from django.urls import path
from . import views

urlpatterns = [
    path('new_dashboard/', views.new_dashboard, name='new_dashboard'),
]