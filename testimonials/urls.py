from django.urls import path
from . import views

urlpatterns = [
    path('', views.testimonials_list, name='testimonials'),
    path('<slug:c_slug>/', views.testimonial_details, name='testimonial_details'),
]
