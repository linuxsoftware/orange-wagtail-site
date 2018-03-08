from django import template
from django.conf import settings
from wagtail.admin.templatetags.wagtailadmin_tags import menu_search

register = template.Library()

@register.simple_tag()
def get_wagtail_site_name():
    return getattr(settings, 'WAGTAIL_SITE_NAME', 'Wagtail')

