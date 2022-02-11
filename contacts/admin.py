from django.contrib import admin

from .models import Contact, Applicant

class ContactAdmin(admin.ModelAdmin):
    list_display =('id', 'name', 'email', 'phone', 'contact_date')
    list_filter = ('email', 'contact_date')
    list_display_links = ('id', 'name')
    search_fields = ('name', 'email')
    list_per_page  = 25

class ApplicantAdmin(admin.ModelAdmin):
    list_display = ('id','first_name', 'last_name', 'contact_num', 'email', 'job_category', 'position', 'cv_file', 'contact_date')
    list_display_links = ('id', 'first_name',  'last_name')
    list_filter = ('position', 'job_category','contact_date', )
    search_fields = ('first_name', 'last_name','email', 'position')
    list_per_page  = 25

admin.site.register(Applicant, ApplicantAdmin)
admin.site.register(Contact, ContactAdmin)