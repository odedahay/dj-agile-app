from ast import keyword
from tkinter.messagebox import NO
from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import News
from taggit.models import Tag
from django.db.models import Count

def news_list(request, tag_slug=None):

    object_list = News.objects.all().filter(status='published')
    tags_list = News.tags.all()

    tag = None

    if tag_slug:
        tag = get_object_or_404(Tag, slug=tag_slug)
        object_list = object_list.filter(tags__in=[tag])
    
    paginator = Paginator(object_list, 6) # 3 posts in each page
    page = request.GET.get('page')
    
    try:
        news_list = paginator.page(page)
    except PageNotAnInteger:
        news_list =paginator.page(1)
    except EmptyPage:
        news_list = paginator.page(paginator.num_pages)

    context = {
        'page':page,
        'news_list':news_list,
        'tag':tag,
        'tags_list':tags_list
    }

    return render(request, 'news/news-list.html', context)


def news_detail(request, c_slug=None):

    news_detail = get_object_or_404(News, slug=c_slug, status='published')
    news_list = News.objects.all().filter(status='published')[:6]

    # Similar News Post
    news_tags_ids = news_detail.tags.values_list('id', flat=True)
    similar_posts = News.objects.all().filter(status='published').filter(tags__in=news_tags_ids).exclude(id=news_detail.id)
    similar_posts = similar_posts.annotate(same_tags=Count('tags')).order_by('-same_tags', 'publish')[:5]
    
    context = {
        'news_detail':news_detail,
        'news_list':news_list,
        'similar_posts':similar_posts
    }

    return render (request, 'news/news-details.html', context)

def search(request, tag_slug=None):
    object_list = News.objects.order_by('-publish').filter(status='published')
    tags_list = News.tags.all()
    tag = None

    if tag_slug:
        tag = get_object_or_404(Tag, slug=tag_slug)
        object_list = object_list.filter(tags__in=[tag])

    if 'keyword' in request.GET:
        keyword = request.GET['keyword']

        if keyword:
            news_list = object_list.filter(content__icontains=keyword)

    context = {
        'news_list':news_list,
        'tag':tag,
        'tags_list':tags_list
    }

    return render(request, 'news/search.html', context)