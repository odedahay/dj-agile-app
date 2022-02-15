from django.db import models
from django.urls import reverse

class Category(models.Model):
    category_name = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=100, unique=True)
    description = models.TextField(max_length=255, blank=True)

    class Meta:
        verbose_name = 'category'
        verbose_name_plural = 'job Categories'

    def get_url(self):
        return reverse('jobs:jobs_by_category', args=[self.slug])

    def __str__(self):
        return self.category_name