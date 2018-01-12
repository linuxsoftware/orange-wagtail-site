from django.db import models
from ls.joyous.models import CalendarPage

# Create a demo version of the Calendar
CalendarPage.is_creatable = False
class DemoCalendarPage(CalendarPage):
    class Meta:
        proxy = True
        verbose_name = "Calendar Demo"

    parent_page_types = ['home.HomePage']
    subpage_types = ['joyous.SimpleEventPage',
                     'joyous.MultidayEventPage',
                     'joyous.RecurringEventPage']

    @classmethod
    def can_create_at(cls, parent):
        # You can only create one of these pages
        return super().can_create_at(parent) and not cls.objects.exists()
