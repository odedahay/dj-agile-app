from django.db import models
from django.urls import reverse
from ckeditor_uploader.fields import RichTextUploadingField

class Page(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.CharField(max_length=200, unique=True)
    content = RichTextUploadingField(blank=True)
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    created_date = models.DateTimeField(auto_now_add=True, null=True)
    is_published = models.BooleanField(default=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering =('title',)
        verbose_name = 'page'
        verbose_name_plural = 'pages'

    def __str__(self):
        return self.title


class Components(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True, null=True)
    content = models.TextField(blank=True)
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    created_date = models.DateTimeField(auto_now_add=True, null=True)
    updated = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=True)

    class Meta:
        ordering = ('title',)
        verbose_name = 'component'
        verbose_name_plural = 'Components'

    # def get_readonly_fields(self, request, obj=None):
    #     if obj:
    #         return ["title"]
    #     else:
    #         return [] 
            
    def __str__(self):
        return self.title

class HeroBanner(models.Model):
    title = models.CharField(max_length=200, unique=True)
    banner_text = models.TextField(blank=True)
    banner_cta_name = models.CharField(max_length=250, blank=True)
    banner_cta_url = models.CharField(max_length=250, blank=True)
    banner_image_desktop = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    banner_image_mobile = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    is_available = models.BooleanField(default=True)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('title',)
        verbose_name = 'banner'
        verbose_name_plural = 'Home Banners'
    
    def __str__(self):
        return self.title


class Assets(models.Model):
    title = models.CharField(max_length=200, unique=True)
    description = models.TextField(blank=True)
    document = models.FileField(upload_to='uploads/', blank=True)
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    is_available = models.BooleanField(default=True)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('title',)
        verbose_name = 'Asset'
        verbose_name_plural = 'Assests'
    
    def __str__(self):
        return self.title