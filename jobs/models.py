from django.db import models
from django.urls import reverse
from job_category.models import Category
from ckeditor.fields import RichTextField

class Job(models.Model):
    job_name = models.CharField(max_length=250, unique=True)
    slug = models.SlugField(max_length=250, unique=True)
    description = RichTextField(blank=True, null=True)
    is_available = models.BooleanField(default=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    created_date = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('-updated',)
        verbose_name = 'job'
        verbose_name_plural = 'job Opportunities'

    def get_url(self):
        return reverse('job_details', args=[self.category.slug, self.slug])

    def __str__(self):
        return self.job_name

