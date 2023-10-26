from django import template

register = template.Library()
# IncludedMasterConsignment__duplicate__
@register.simple_tag
def remove_roots(value):
    return value.replace("root/root/", "").replace("__duplicate__", "")
