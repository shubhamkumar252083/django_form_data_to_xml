from django import template

register = template.Library()

@register.filter
def remove_roots(value):
    return value[::-1]

