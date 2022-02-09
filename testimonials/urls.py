from django.urls import path
from . import views

app_name ='testimonials'

urlpatterns = [
    path('', views.testimonials_list, name='testimonials_list'),
    path('<slug:c_slug>/', views.testimonial_details, name='testimonial_details'), 
]
