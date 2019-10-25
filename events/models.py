from django.db import models
from django.conf import settings
from django.dispatch import receiver
from wagtail.admin.signals import init_new_page
from wagtail.core.models import Page
from wagtail.core.fields import RichTextField
from wagtail.admin.edit_handlers import (FieldPanel, MultiFieldPanel,
        PageChooserPanel)
from ls.joyous.models import CalendarPage
from ls.joyous.models import (SimpleEventPage, MultidayEventPage,
        RecurringEventPage, ExtraInfoPage, CancellationPage,
        PostponementPage)
from ls.joyous.models.events import HiddenNumDaysPanel
from ls.joyous.utils.mixins import ProxyPageMixin
from ls.joyous.edit_handlers import ExceptionDatePanel
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

############################################################################

# Experimenting with inheriting event models

CalendarPage.subpage_types = ["events.DemoSimpleEventPage",
                              "events.DemoMultidayEventPage",
                              "events.DemoRecurringEventPage",
                              "events.DemoMultidayRecurringEventPage", ]

class DemoSimpleEventPage(SimpleEventPage):
    organizer = models.CharField(max_length=100, blank=True)

    content_panels = SimpleEventPage.content_panels + [
        FieldPanel('organizer'),
        ]

class DemoMultidayEventPage(MultidayEventPage):
    organizer = models.CharField(max_length=100, blank=True)

    content_panels = MultidayEventPage.content_panels + [
        FieldPanel('organizer'),
        ]

# Panel trickery needed as editing proxy models doesn't work yet :-(
# Alternatively don't make DemoMultidayRecurringEventPage and
# DemoRescheduleMultidayEventPage proxy models
class DemoHiddenNumDaysPanel(HiddenNumDaysPanel):
    def _show(self):
        retval = super()._show()
        page = getattr(self, 'instance', None)
        if isinstance(page, (DemoMultidayRecurringEventPage,
                             DemoRescheduleMultidayEventPage)):
            retval = True
        return retval

class DemoRecurringEventPage(RecurringEventPage):
    organizer = models.CharField(max_length=100, blank=True)

    subpage_types = ["events.DemoExtraInfoPage",
                     "events.DemoCancellationPage",
                     "events.DemoPostponementPage"]
    content_panels = RecurringEventPage.content_panels0 +  \
                     [ DemoHiddenNumDaysPanel() ] +        \
                     RecurringEventPage.content_panels1 +  \
                     [ FieldPanel('organizer'), ]

class DemoMultidayRecurringEventPage(ProxyPageMixin, DemoRecurringEventPage):
    subpage_types = ["events.DemoExtraInfoPage",
                     "events.DemoCancellationPage",
                     "events.DemoRescheduleMultidayEventPage"]
    template = "events/demo_recurring_event_page.html"
    content_panels = RecurringEventPage.content_panels0 +  \
                     [ FieldPanel('num_days') ] +          \
                     RecurringEventPage.content_panels1 +  \
                     [ FieldPanel('organizer'), ]

class DemoExtraInfoPage(ProxyPageMixin, ExtraInfoPage):
    parent_page_types = ["events.DemoRecurringEventPage",
                         "events.DemoMultidayRecurringEventPage"]

class DemoCancellationPage(ProxyPageMixin, CancellationPage):
    parent_page_types = ["events.DemoRecurringEventPage",
                         "events.DemoMultidayRecurringEventPage"]

class DemoPostponementPage(PostponementPage):
    # allow the organizer to be changed when there is a postponement
    organizer = models.CharField(max_length=100, blank=True)

    parent_page_types = ["events.DemoRecurringEventPage" ]
    postponement_panel = MultiFieldPanel(
            PostponementPage.postponement_panel0 +
            [ DemoHiddenNumDaysPanel() ] +        \
            PostponementPage.postponement_panel1 +
            [ FieldPanel('organizer'), ],
            heading="Postponed to")
    content_panels = [
        PageChooserPanel('overrides'),
        ExceptionDatePanel('except_date'),
        PostponementPage.cancellation_panel,
        postponement_panel,
    ]

    def serveCancellation(self, request):
        response = super().serveCancellation(request)
        response.template_name = "events/demo_postponement_page_from.html"
        return response

@receiver(init_new_page)
def copyOrganizer(sender, **kwargs):
    page = kwargs.get('page')
    parent = kwargs.get('parent')
    if (isinstance(page, DemoPostponementPage) and
        isinstance(parent, DemoRecurringEventPage) and
        not page.organizer):
        page.organizer = parent.organizer

class DemoRescheduleMultidayEventPage(ProxyPageMixin, DemoPostponementPage):
    template = "events/demo_postponement_page.html"
    parent_page_types = ["events.DemoMultidayRecurringEventPage"]
    postponement_panel = MultiFieldPanel(
            PostponementPage.postponement_panel0 +
            [FieldPanel('num_days')] +
            PostponementPage.postponement_panel1 +
            [ FieldPanel('organizer'), ],
            heading="Postponed to")
    content_panels = [
        PageChooserPanel('overrides'),
        ExceptionDatePanel('except_date'),
        PostponementPage.cancellation_panel,
        postponement_panel,
    ]

