from django.urls import path
from . import views

urlpatterns = [
    path('', views.inquiry, name='inquiry'),
    path('thank-you/', views.thank_you, name='thank_you'),
    path('applicant/', views.applicant, name='applicant'),
    path('applicant/thank-you/', views.job_applicant, name='job_thank_you'),
]
