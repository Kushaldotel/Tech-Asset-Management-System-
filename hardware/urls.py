from django.urls import path
from . import views

urlpatterns = [
    path('naya/',views.Index,name='naya-naulo')
]
