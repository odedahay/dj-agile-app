
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', include('pages.urls')),
    path('news/', include('news.urls', namespace='news')),
    path('testimonials/', include('testimonials.urls', namespace='testimonials')),
    path('contact-us/', include('contacts.urls')),
    path('jobs/', include('jobs.urls')),
    path('admin/', admin.site.urls),
    path('ckeditor/', include('ckeditor_uploader.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
