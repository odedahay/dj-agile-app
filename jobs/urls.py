from django.urls import path
from . import views

app_name='jobs'

urlpatterns = [
    path('', views.jobs, name='jobs_list'),
    path('<slug:category_slug>/', views.jobs, name='jobs_by_category'),
    path('<slug:category_slug>/<slug:job_slug>/', views.job_details, name='job_details'),
    path('<slug:category_slug>/<slug:job_slug>/share/', views.job_details, name='job_share'),
]
