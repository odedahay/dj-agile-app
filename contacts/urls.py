from django.urls import path
from . import views

urlpatterns = [
    path('', views.inquiry, name='inquiry'),
    path('applicant/', views.applicant, name='applicant'),
    path('thank-you/', views.thank_you, name='thank_you')
]
