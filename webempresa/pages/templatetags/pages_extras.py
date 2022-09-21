from atexit import register
import re
from django import template
from pages.models import Page

register = template.Library()

@register.simple_tag              # transformamos una funcion normal en un tag simple 

def get_page_list():
    pages = Page.objects.all()
    return pages