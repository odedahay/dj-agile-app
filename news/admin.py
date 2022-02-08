from django.contrib import admin

from . models import News

class NewsAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'status', 'author')
    #list_display = ('title', 'slug', 'author', 'publish', 'status')
    list_filter = ('status', 'created', 'status', 'author')
    list_display_links = ('title',)
    list_editable = ('slug','status',)

    prepopulated_fields = {'slug': ('title',)}
    date_hierarchy = 'publish'
    ordering = ('status', 'publish')
    search_fields = ('title',)
    list_per_page = 25


admin.site.register(News, NewsAdmin)