# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool


class TilesContainerPlugin(CMSPluginBase):
    module = "Components"
    name = "Tiles container"
    render_template = "tiles_container/template.html"
    cache = False
    allow_children = True
    child_classes = ['TileComponentPlugin', ]


plugin_pool.register_plugin(TilesContainerPlugin)
