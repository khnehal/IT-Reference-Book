# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2019-01-22 15:17
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import djangocms_text_ckeditor.fields
import filer.fields.image


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('cms', '0020_old_tree_cleanup'),
        migrations.swappable_dependency(settings.FILER_IMAGE_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='ImageSlider',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, related_name='header_component_imageslider', serialize=False, to='cms.CMSPlugin')),
                ('title', djangocms_text_ckeditor.fields.HTMLField(blank=True, help_text='Enter the title of the image here', null=True, verbose_name='Carousel title')),
                ('description', djangocms_text_ckeditor.fields.HTMLField(blank=True, help_text='Enter a description for the item here', null=True, verbose_name='Carousel Description')),
                ('is_internal_link', models.BooleanField(default=False)),
                ('external_url', models.CharField(blank=True, default='', max_length=400, null=True)),
                ('btn_text', models.CharField(blank=True, help_text='Specify the name that you want to appear in the button (max 60 characters)', max_length=60, verbose_name='Specify Name')),
                ('image_filer', filer.fields.image.FilerImageField(blank=True, help_text='Insert an image for the slider', max_length=1000, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.FILER_IMAGE_MODEL, verbose_name='Image')),
                ('internal_url', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Internal', to='cms.Page')),
            ],
            options={
                'verbose_name': 'Slide',
                'verbose_name_plural': 'Slide',
            },
            bases=('cms.cmsplugin',),
        ),
        migrations.CreateModel(
            name='Slider',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, related_name='header_component_slider', serialize=False, to='cms.CMSPlugin')),
            ],
            options={
                'verbose_name': 'Header Component',
                'verbose_name_plural': 'Header Component',
            },
            bases=('cms.cmsplugin',),
        ),
    ]
