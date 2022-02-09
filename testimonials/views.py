from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import Testimonial

def testimonials_list(request):
    object_list = Testimonial.objects.all().filter(status='published')

    paginator = Paginator(object_list, 12)
    page = request.GET.get('page')

    try:
        testimonials_pagination = paginator.page(page)
    except PageNotAnInteger:
        testimonials_pagination = paginator.page(1)
    except EmptyPage:
        testimonials_pagination = paginator.page(paginator.num_pages)

    context = {
        'page':page,
        'testimonials_pagination':testimonials_pagination,
        'testimonials_list':object_list
    }

    return render(request, 'testimonials/testimonials.html', context)

def testimonial_details(request, c_slug=None):

    testimonial_detail = get_object_or_404(Testimonial, slug=c_slug, status='published')
    testimonials_list = Testimonial.objects.all().filter(status='published')[:6]
    
    context = {
        'testimonial_detail': testimonial_detail,
        'testimonials_list': testimonials_list
    }
    return render(request, 'testimonials/testimonial-details.html', context)
