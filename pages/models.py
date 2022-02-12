from distutils.command.upload import upload
from pyexpat import model
from statistics import mode
from turtle import title
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
    body = models.TextField(blank=True)
    photo = models.ImageField(upload_to='photos/%Y/%m/%d', blank=True)
    created_date = models.DateTimeField(auto_now_add=True, null=True)
    updated = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=True)

    class Meta:
        ordering = ('title',)
        verbose_name = 'component'
        verbose_name_plural = 'Components'
    
    def __str__(self):
        return self.title

