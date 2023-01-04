from django import template                                                                                                                                                        
from django.template.defaultfilters import stringfilter

register = template.Library()

@register.filter
@stringfilter
def space2Dash(s):
    return s.replace(' ', '_');