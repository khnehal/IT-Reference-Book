# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool


class HeaderPlugin(CMSPluginBase):
    module = "Components"
    name = "Header container"
    render_template = "header_component/template.html"
    cache = False
    allow_children = True


plugin_pool.register_plugin(HeaderPlugin)
