from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from import_export import resources
from .models import Contact, Applicant


class ApplicantResources(resources.ModelResource):
    class Meta:
        model = Applicant

class ContactResources(resources.ModelResource):
    class Meta:
        model = Contact

class ContactAdmin(ImportExportModelAdmin):
    resources_class=ContactResources

    list_display =( 'name', 'email', 'phone', 'contact_date')
    list_filter = ('contact_date',)
    list_display_links = ( 'name',)
    search_fields = ('name', 'email')
    list_per_page  = 25

class ApplicantAdmin(ImportExportModelAdmin):
    resource_class = ApplicantResources

    list_display = ('first_name', 'last_name', 'contact_num', 'email', 'job_category', 'position', 'cv_file', 'contact_date')
    list_display_links = ( 'first_name',  'last_name')
    list_filter = ('position', 'job_category', 'contact_date', )
    search_fields = ('first_name', 'last_name','email', 'position')
    list_per_page  = 25

admin.site.register(Applicant, ApplicantAdmin)
admin.site.register(Contact, ContactAdmin)