from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from datetime import datetime
from django.urls import reverse
from ckeditor_uploader.fields import RichTextUploadingField
from taggit.managers import TaggableManager


class News(models.Model):

    STATUS_CHOICES = (
        ('draft', 'Draft'),
        ('published', 'Published'),
    )

    title = models.CharField(max_length=250, unique=True, null=True)
    slug = models.CharField(max_length=250, unique=True, null=True)
    author = models.ForeignKey(User, on_delete=models.PROTECT, related_name='news_posts',  null=True)
    content = RichTextUploadingField(blank=True, null=True)
    photo = models.ImageField(upload_to='photo/%Y/%m/%d/', blank=True)
    #pub_date = models.DateTimeField(default=datetime.now, blank=True)
    created = models.DateTimeField(auto_now_add=True, null=True)
    publish = models.DateTimeField(default=timezone.now, null=True)
    # is_published = models.BooleanField(default=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='draft')
    tags = TaggableManager()


    def get_absolute_url(self):
        return reverse("news:news_detail", args=[self.slug])
    

    class Meta:
        ordering = ('-created',)
        verbose_name = 'news'
        verbose_name_plural = 'news'

    def __str__(self):
        return self.title