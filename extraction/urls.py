from django.urls import path
from . import views

app_name = 'app'

urlpatterns = [
    path('upload/', views.upload_zip, name='upload'),
]
