from django.db import models
from ls.joyous.models import CalendarPage

# Create a demo version of the Calendar
CalendarPage.is_creatable = False

class DemoCalendarPage(CalendarPage):
    class Meta:
        proxy = True
        verbose_name = "Calendar Demo"

    parent_page_types = ['home.HomePage']
