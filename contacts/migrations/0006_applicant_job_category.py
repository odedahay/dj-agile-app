# Generated by Django 4.0.2 on 2022-02-11 12:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0005_applicant_job_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='applicant',
            name='job_category',
            field=models.CharField(max_length=150, null=True),
        ),
    ]
