from django.db import models
from django.conf import settings
from wagtail.core.models import Page
from wagtail.core.fields import RichTextField
from wagtail.admin.edit_handlers import FieldPanel
from ls.joyous.models import CalendarPage

#from ls.joyous.models import SpecificCalendarPage, GeneralCalendarPage
#CalendarPage.is_creatable = True
#SpecificCalendarPage.is_creatable = True
#GeneralCalendarPage.is_creatable = True

# Create a demo version of the Calendar
CalendarPage.is_creatable = False

class DemoCalendarPage(CalendarPage):
    class Meta:
        proxy = True
        verbose_name = "Calendar Demo"

    parent_page_types = ['home.HomePage']


class TagsDemoPage(Page):
    welcome = RichTextField(default='', blank=True)
    welcome.help_text = "A welcome message"
    content = RichTextField(default='', blank=True)
    content.help_text = "An area of text for whatever you like"

    content_panels = Page.content_panels + [
        FieldPanel('welcome', classname="full"),
        FieldPanel('content', classname="full"),
        ]

    def get_context(self, request, *args, **kwargs):
        retval = super().get_context(request, *args, **kwargs)
        retval['themeCSS'] = getattr(settings, "JOYOUS_THEME_CSS", "")
        return retval


