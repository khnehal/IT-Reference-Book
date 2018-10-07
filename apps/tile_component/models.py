from django.db import models
from cms.models import CMSPlugin
from cms.utils.compat.dj import python_2_unicode_compatible

from cms.models.pagemodel import Page
from filer.fields.image import FilerImageField


@python_2_unicode_compatible
class TileComponentModel(CMSPlugin):

    tile_title = models.CharField(max_length=250)
    has_image = models.BooleanField(default=False)
    img_alt_text = models.CharField(max_length=250, blank=True, default='')
    image = FilerImageField(
        verbose_name=('Image'),
        null=True,
        blank=True,
        max_length=1000,
        on_delete=models.SET_NULL,
    )

    link_to_page = models.ForeignKey(
        Page,
        blank=True,
        null=True,
        related_name="tile_component",
        limit_choices_to={'publisher_is_draft': True},
        help_text='Specify the page to which this tile will redirect.'
    )

    class Meta:
        verbose_name = 'Tile Component'
        verbose_name_plural = 'Tile Component'
        app_label = 'tile_component'

    def __str__(self):
        """Return id."""
        return str(self.id)
