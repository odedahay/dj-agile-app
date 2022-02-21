from re import A
from django.contrib import admin
from .models import Page, Components, HeroBanner, Assets


class PagesAdmin(admin.ModelAdmin):
    list_display = ('id','title', 'slug', 'created_date', 'updated','is_published')
    list_display_links = ('id','title',)
    list_editable = ('is_published',)
    prepopulated_fields = {'slug': ('title',)}

class ComponentAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'slug','updated')
    list_display_links = ('id','title',)
    prepopulated_fields = {'slug': ('title',)}

    # def get_readonly_fields(self, request, obj=None):
    #     defaults = super().get_readonly_fields(request, obj=obj)
    #     if obj:  # if we are updating an object
    #         defaults = tuple(defaults) + ('title', )  # make sure defaults is a tuple
    #     return defaults

    def get_readonly_fields(self, request, obj=None):
        if obj:
            self.prepopulated_fields = {}
            return self.readonly_fields + ('slug',)
        return self.readonly_fields

class AssetsAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'updated_date', 'is_available')
    list_display_links = ('id','title',)
    list_editable = ('is_available',)

admin.site.register(Assets, AssetsAdmin)
admin.site.register(HeroBanner)
admin.site.register(Components, ComponentAdmin)
admin.site.register(Page, PagesAdmin)
