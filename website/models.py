# ------------------------------------------------------------------------------
# Website models
# ------------------------------------------------------------------------------

from django.db import models
from django import forms
from wagtail.core.models import Page
from wagtail.core.fields import RichTextField
from wagtail.admin.edit_handlers import FieldPanel

# ------------------------------------------------------------------------------
# Website Pages
# ------------------------------------------------------------------------------
class PlainPage(Page):
    class Meta:
        verbose_name = "Plain Text Page"

    content = RichTextField(default='', blank=True)
    content.help_text = "An area of text for whatever you like"

    content_panels = Page.content_panels + [
        FieldPanel('content', classname="full"),
        ]

