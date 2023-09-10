from django.urls import path

from . import views

app_name = 'details'

urlpatterns = [
    path('upload-csv/', views.upload_csv, name='upload-csv'),
    path('generate-seating-plan/', views.generate_seating_plan, name='generate-seating-plan'),
    #path('generate-seating-plan2/', views.generate_seating_plan2, name='generate-seating-plan2'),
]
