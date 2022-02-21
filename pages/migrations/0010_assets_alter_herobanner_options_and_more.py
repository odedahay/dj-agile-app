# Generated by Django 4.0.2 on 2022-02-18 15:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0009_herobanner'),
    ]

    operations = [
        migrations.CreateModel(
            name='Assets',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, unique=True)),
                ('description', models.TextField(blank=True)),
                ('document', models.FileField(blank=True, upload_to='uploads/')),
                ('photo', models.ImageField(blank=True, upload_to='photos/%Y/%m/%d/')),
                ('is_available', models.BooleanField(default=True)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('updated_date', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Asset',
                'verbose_name_plural': 'Assests',
                'ordering': ('title',),
            },
        ),
        migrations.AlterModelOptions(
            name='herobanner',
            options={'ordering': ('title',), 'verbose_name': 'banner', 'verbose_name_plural': 'Home Banners'},
        ),
        migrations.AlterField(
            model_name='components',
            name='photo',
            field=models.ImageField(blank=True, upload_to='photos/%Y/%m/%d/'),
        ),
        migrations.AlterField(
            model_name='herobanner',
            name='banner_image_desktop',
            field=models.ImageField(blank=True, upload_to='photos/%Y/%m/%d/'),
        ),
        migrations.AlterField(
            model_name='herobanner',
            name='banner_image_mobile',
            field=models.ImageField(blank=True, upload_to='photos/%Y/%m/%d/'),
        ),
    ]