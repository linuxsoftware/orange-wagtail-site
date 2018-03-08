# ------------------------------------------------------------------------------
# Homepage models
# ------------------------------------------------------------------------------

from django.db import models
from wagtail.core.models import Page, Orderable
from wagtail.core.fields import RichTextField
from wagtail.admin.edit_handlers import FieldPanel, MultiFieldPanel, \
    InlinePanel, PageChooserPanel
from modelcluster.fields import ParentalKey


class HomePageHighlight(Orderable):
    homepage = ParentalKey('home.HomePage',
                           on_delete=models.CASCADE,
                           related_name='highlights')
    title = models.CharField("Title", max_length=80, blank=True)
    blurb = RichTextField(default='', blank=True)
    page  = models.ForeignKey('wagtailcore.Page',
                              null=True, blank=True,
                              on_delete=models.CASCADE,
                              related_name='+')

    panels = [FieldPanel('title', classname="full title"),
              FieldPanel('blurb', classname="full"),
              PageChooserPanel('page'), ]


class HomePage(Page):
    parent_page_types = []

    welcome = RichTextField(default='', blank=True)
    welcome.help_text = "A short introductory message"
    content = RichTextField(default='', blank=True)
    content.help_text = "An area of text for whatever you like"

    # HomePage is a bit different to other pages as the title is not displayed
    content_panels = [
        FieldPanel('welcome', classname="full"),
        MultiFieldPanel([InlinePanel('highlights')],
                        heading="Highlights",
                        classname="collapsible"),
        FieldPanel('content', classname="full"),
        ]
