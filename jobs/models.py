from django.db import models
from django.urls import reverse
from ckeditor.fields import RichTextField

class JobCategory(models.Model):
    category_name = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=100, unique=True)
    description = models.TextField(max_length=255, blank=True)

    class Meta:
        verbose_name = 'category'
        verbose_name_plural = 'Categories'

    def get_url(self):
        return reverse('jobs:jobs_by_category', args=[self.slug])

    def __str__(self):
        return self.category_name

class Job(models.Model):
    job_name = models.CharField(max_length=250, unique=True)
    slug = models.SlugField(max_length=250, unique=True)
    description = RichTextField(blank=True, null=True)
    is_available = models.BooleanField(default=True)
    category = models.ForeignKey(JobCategory, on_delete=models.CASCADE)
    created_date = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('-updated',)
        verbose_name = 'job'
        verbose_name_plural = 'jobs'

    def get_url(self):
        return reverse('jobs:job_details', args=[self.category.slug, self.slug])
    
    def share_url(self):
        return reverse('jobs:job_share', args=[self.category.slug, self.slug])

    def __str__(self):
        return self.job_name

