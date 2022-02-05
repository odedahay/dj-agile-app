from django.shortcuts import render

def news_list(request):
    return render(request, 'news/news-list.html')


def news_detail(request, c_slug=None):
    return render (request, 'news/news-details.html')