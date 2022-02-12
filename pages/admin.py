from django.contrib import admin
from .models import Page, Components


class PagesAdmin(admin.ModelAdmin):
    list_display = ('id','title', 'slug', 'created_date', 'updated','is_published')
    list_display_links = ('id','title',)
    list_editable = ('is_published',)
    prepopulated_fields = {'slug': ('title',)}

class ComponentAdmin(admin.ModelAdmin):
    list_display = ('id', 'title',)
    list_display_links = ('id','title',)

admin.site.register(Components, ComponentAdmin)
admin.site.register(Page, PagesAdmin)
