# Generated by Django 4.0.2 on 2022-02-11 10:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0004_alter_applicant_options_alter_contact_options_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='applicant',
            name='job_id',
            field=models.IntegerField(null=True),
        ),
    ]
