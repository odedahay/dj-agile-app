from .models import JobCategory

def menu_links(request):
    links = JobCategory.objects.all()
    return dict(links=links)