from django.urls import path

from . import views

app_name = 'details'

urlpatterns = [
    path('upload-csv/', views.upload_csv, name='upload-csv'),
    path('generate-seating-plan/', views.generate_seating_plan, name='generate-seating-plan'),
    path('generate-seating-plan2/', views.generate_seating_plan2, name='generate-seating-plan2'),
    path('generate-seating-plan3/', views.generate_seating_plan3, name='generate-seating-plan3'),
    path('generate-seating-plan4/', views.generate_seating_plan4, name='generate-seating-plan4'),
    path('', views.home_page, name='home'),

]
