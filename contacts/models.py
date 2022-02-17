from re import I
from django.db import models
from datetime import datetime
from django.shortcuts import render, get_object_or_404
from jobs.models import Job

class Contact(models.Model):
    name = models.CharField(max_length=250)
    email = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    message = models.TextField(null=True, blank=True)
    contact_date = models.DateTimeField(default=datetime.now, blank=True)

    class Meta:
        ordering = ('-contact_date',)
        verbose_name = 'Enquiry'
        verbose_name_plural = 'Enquiries'

    def __str__(self):
        return self.name


class Applicant(models.Model):
    first_name = models.CharField(max_length=250)
    last_name = models.CharField(max_length=250)
    contact_num = models.CharField(max_length=100)
    email = models.CharField(max_length=100, null=True)
    position = models.CharField(max_length=100)
    cv_file = models.FileField(upload_to='uploads/cvs/', null=True, blank=True)
    message = models.TextField(null=True, blank=True)
    contact_date = models.DateTimeField(default=datetime.now, blank=True)
    job_id = models.IntegerField(null=True)
    job_category = models.CharField(max_length=150, null=True)

    class Meta:
        ordering = ('-contact_date',)
        verbose_name = 'Applicant'
        verbose_name_plural = 'Applicants'

    def __str__(self):
        return self.first_name
