from statistics import mode
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

