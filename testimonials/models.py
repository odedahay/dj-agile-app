from django.db import models
from django.utils import timezone
from django.urls import reverse
from ckeditor_uploader.fields import RichTextUploadingField


class Testimonial(models.Model):
    STATUS_CHOICES = (
        ('draft', 'Draft'),
        ('published', 'Published'),
    )

    name = models.CharField(max_length=250, unique=True, null=True)
    slug = models.CharField(max_length=250, unique=True, null=True)
    designation = models.CharField(max_length=250, blank=True)
    content = RichTextUploadingField(blank=True, null=True)
    order_by = models.IntegerField(unique=True, blank=True, null=True)
    image = models.ImageField(upload_to='photos/%Y/%m/%d', blank=True)
    status = models.CharField(max_length=15, choices=STATUS_CHOICES, default='draft')
    created = models.DateTimeField(auto_now_add=True, null=True)
    publish = models.DateTimeField(default=timezone.now, null=True)

    def get_absolute_url(self):
        return reverse("testimonials:testimonial_details", args=[self.slug])
    
    class Meta:
        ordering = ('-created',)
        verbose_name = 'testimonial'
        verbose_name_plural = 'testimonials'

    def __str__(self):
        return self.name