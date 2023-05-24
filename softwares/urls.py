from django.urls import path
from . import views

urlpatterns = [
    path('new_soft/', views.new_soft, name='new_soft'),
]