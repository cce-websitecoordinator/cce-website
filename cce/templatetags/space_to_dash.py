from django import template

register = template.Library()

@register.filter(name='space2Dash')
def space2Dash(s):
    return s.replace(' ', '_');