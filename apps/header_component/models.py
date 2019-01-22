# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

from django.utils.encoding import python_2_unicode_compatible
from django.utils.translation import ugettext_lazy as _
from cms.models import CMSPlugin

from cms.models.pagemodel import Page

from filer.fields.image import FilerImageField

from djangocms_text_ckeditor.fields import HTMLField


@python_2_unicode_compatible
class Slider(CMSPlugin):
    class Meta:
        app_label = "header_component"
        verbose_name = "Header Component"
        verbose_name_plural = "Header Component"

    def __str__(self):
        """Return title."""
        return "Header Component"


@python_2_unicode_compatible
class ImageSlider(CMSPlugin):

    title = HTMLField(
        _('Carousel title'),
        blank=True,
        null=True,
        help_text='Enter the title of the image here',)

    description = HTMLField(
        _('Carousel Description'),
        blank=True,
        null=True,
        help_text='Enter a description for the item here',)

    image_filer = FilerImageField(
        verbose_name=_("Image"),
        null=True,
        blank=True,
        max_length=1000,
        on_delete=models.SET_NULL,
        help_text='Insert an image for the slider')

    is_internal_link = models.BooleanField(
        blank=True,
        default=False,)

    internal_url = models.ForeignKey(
        Page,
        blank=True,
        null=True,
        related_name='Internal',
        limit_choices_to={
            'publisher_is_draft': True,
        },
    )

    external_url = models.CharField(
        blank=True,
        null=True,
        max_length=400,
        default="",)

    btn_text = models.CharField(
        max_length=60,
        verbose_name='Specify Name',
        blank=True,
        help_text='Specify the name that you want to appear in the button (max 60 characters)',)

    class Meta:
        app_label = 'header_component'
        verbose_name = "Slide"
        verbose_name_plural = "Slide"

    def __str__(self):
        """Return title."""
        return self.title
