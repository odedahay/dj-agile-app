# Generated by Django 4.0.2 on 2022-02-12 06:25

import ckeditor_uploader.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0004_components_created_date_components_is_published_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='components',
            name='body',
            field=ckeditor_uploader.fields.RichTextUploadingField(blank=True),
        ),
    ]
