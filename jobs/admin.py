from django.contrib import admin
from .models import Job

class JobAdmin(admin.ModelAdmin):
    list_display = ('job_name', 'category', 'updated', 'is_available')
    list_editable = ('category','is_available',)
    prepopulated_fields = {'slug': ('job_name',)}

admin.site.register(Job, JobAdmin)