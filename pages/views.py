from django.shortcuts import render
from testimonials.models import Testimonial
from news.models import News
from .models import Page, Components

def index(request):
    latest_testimonials = Testimonial.objects.all().filter(status='published')[:3]
    latest_news = News.objects.all().filter(status='published')[:2]

    context = {
        'latest_testimonials':latest_testimonials,
        'latest_news': latest_news
    }
    return render(request, 'pages/index.html', context)


def about(request):
    page = Page.objects.filter(slug__exact='about')

    context = {
        'page': page
    }
    return render(request, 'pages/about.html', context)


def policy(request):
    page = Page.objects.filter(slug__exact='policy')
    
    context = {
        'page': page
    }

    return render(request, 'pages/policy.html', context)


def comp_footer(request):

    footer = Components.objects.filter(title__exact='footer')

    context ={
        'footer': footer
    }
    return render(request, 'base.html', context)