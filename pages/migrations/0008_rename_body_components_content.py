# Generated by Django 4.0.2 on 2022-02-16 16:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0007_alter_components_body'),
    ]

    operations = [
        migrations.RenameField(
            model_name='components',
            old_name='body',
            new_name='content',
        ),
    ]
