from unicodedata import category
from django.shortcuts import render, get_object_or_404
from job_category.models import Category
from .models import Job

def jobs(request, category_slug=None):

    categories = None
    jobs = None

    if category_slug != None:
        categories = get_object_or_404(Category, slug=category_slug)
        jobs = Job.objects.filter(category=categories, is_available=True)
        jobs_count = jobs.count()
    else:
        jobs = Job.objects.all().filter(is_available=True)
        jobs_count = jobs.count()

    context = {
        'categories':categories,
        'jobs': jobs,
        'jobs_count': jobs_count,
    }
    return render(request, 'jobs/jobs_list.html', context)

def job_details(request, category_slug, job_slug):

    try:
        single_job = Job.objects.get(category__slug=category_slug, slug=job_slug)
    except Exception as e:
        raise e

    context = {
        'single_job': single_job
    }
    return render(request, 'jobs/job_details.html', context)