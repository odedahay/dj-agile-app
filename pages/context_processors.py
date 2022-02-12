from . models import Components

def comp_footer(request):
    footer = Components.objects.filter(title__exact='footer')
    return {'footer': footer}