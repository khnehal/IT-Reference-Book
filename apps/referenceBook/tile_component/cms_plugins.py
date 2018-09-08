# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool

from .models import TileComponentModel


class TileComponentPlugin(CMSPluginBase):
    module = "Components"
    name = "Tile Component Plugin"
    render_template = "tile_component/template.html"
    model = TileComponentModel
    cache = False
    require_parent = True
    parent_classes = ['TilesContainerPlugin', ]


plugin_pool.register_plugin(TileComponentPlugin)
