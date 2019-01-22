# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool

from .models import Slider, ImageSlider


class SliderInline(admin.StackedInline):
    module = "Components"
    model = ImageSlider
    extra = 0
    min_num = 0


class SliderPlugin(CMSPluginBase):
    module = "Components"
    model = ImageSlider
    name = "Image Slide"
    cache = False
    require_parent = True
    parent_classes = ['HeaderPlugin', ]
    render_template = "header_component/template.html"


class HeaderPlugin(CMSPluginBase):
    module = "Components"
    model = Slider
    name = "Header container"
    render_template = "header_component/template.html"
    cache = False
    allow_children = True
    child_classes = ['SliderPlugin', ]
    inlines = [SliderInline, ]


plugin_pool.register_plugin(SliderPlugin)
plugin_pool.register_plugin(HeaderPlugin)
