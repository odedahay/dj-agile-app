from django.urls import path
from . import views

urlpatterns = [
    path('', views.jobs, name='jobs'),
    path('<slug:category_slug>/', views.jobs, name='jobs_by_category'),
    path('<slug:category_slug>/<slug:job_slug>/', views.job_details, name='job_details'),
]
