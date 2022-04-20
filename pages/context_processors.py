from . models import Components, Assets

def comp_footer(request):
    footer = Components.objects.filter(slug__exact="footer-section")
    return {'footer': footer}

def comp_contact_section(request):
    contact_details_section = Components.objects.filter(slug__exact="contact-details-section")
    return {'contact_details_section': contact_details_section}

def form_applicant(request):
    form_applicant = Assets.objects.filter(id__exact=1, is_available=True)
    return {'form_applicant': form_applicant}
