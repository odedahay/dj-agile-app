from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404
from .models import Job, JobCategory
from .forms import EmailJobForm
from django.core.mail import send_mail
from django.conf import settings
from django.shortcuts import HttpResponse


def jobs(request, category_slug=None):

    categories = None
    jobs = None

    if category_slug != None:
        categories = get_object_or_404(JobCategory, slug=category_slug)
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
    
def is_ajax(request):
    return request.META.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest'

def job_details(request, category_slug, job_slug):

    try:
        single_job = Job.objects.get(category__slug=category_slug, slug=job_slug, is_available=True)
        post_job = get_object_or_404(Job, slug=job_slug, is_available=True)

        # Share this job widget
        # sent = False
        
        # if request.method == 'POST':
        #     # Form was submitted
        #     form = EmailJobForm(request.POST)

        #     if form.is_valid():
        #         # Form fields passed validation
        #         cd = form.cleaned_data
        #         email_provider = settings.EMAIL_HOST_USER
            
        #         post_url = request.build_absolute_uri(post_job.get_url())
        #         subject = f"{cd['name']} recommends you read " f"{post_job.job_name}"
        #         message = f"AGILE CREW\'s job post for {post_job.job_name}, read more at {post_url}\n\n" f"{cd['name']}\'s comments: {cd['comments']}"
        #         send_mail(subject, message, email_provider, [cd['to']])

        #         sent = True

        # else:

        #     form = EmailJobForm()
        if is_ajax(request=request):
            form = EmailJobForm(request.POST)

            if form.is_valid():
                cd = form.cleaned_data
                email_provider = settings.EMAIL_HOST_USER
            
                post_url = request.build_absolute_uri(post_job.get_url())
                subject = f"{cd['name']} recommends you read " f"{post_job.job_name}"
                message = f"AGILE CREW\'s job post for {post_job.job_name}, read more at {post_url}\n\n" f"{cd['name']}\'s comments: {cd['comments']}"
                send_mail(subject, message, email_provider, [cd['to']])

                return JsonResponse({
                    'msg':'Success'
                })
                
        else:
            form = EmailJobForm()

    except Exception as e:
        raise e

    context = {
        'single_job': single_job,
        'post_job':post_job,
        'form': form,
    }

    return render(request, 'jobs/job_details.html', context)