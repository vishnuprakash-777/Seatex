from django.urls import path
from . import views
from .views import upload_csv

app_name = 'details'

urlpatterns = [
    path('upload-csv/', upload_csv, name='upload-csv'),
]

