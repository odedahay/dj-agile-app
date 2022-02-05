
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('pages.urls')),
    path('news/', include('news.urls')),
    path('testimonials/', include('testimonials.urls')),
    path('admin/', admin.site.urls),
]
