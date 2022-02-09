import imp
from django.contrib import admin

from .models import Testimonial

class TestimonialsAdmin(admin.ModelAdmin):
    list_display = ('name', 'order_by', 'created', 'status',)
    list_display_links = ('name',)
    list_editable = ('order_by','status',)
    list_filter = ('status', 'created', 'status',)
    
    prepopulated_fields = {'slug': ('name',)}
    date_hierarchy = 'publish'
    search_fields = ('name',)
    list_per_page = 25

admin.site.register(Testimonial, TestimonialsAdmin)
