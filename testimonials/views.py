from django.shortcuts import render

def testimonials_list(request):
    return render(request, 'testimonials/testimonials.html')

def testimonial_details(request, c_slug=None):
    return render(request, 'testimonials/testimonial-details.html')
