from django.db import models
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
