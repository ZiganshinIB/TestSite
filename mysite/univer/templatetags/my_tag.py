from django import template
from univer.models import GroupC

register = template.Library()


@register.simple_tag
def get_groups():
    return GroupC.objects.all()


# EXAMPLE:
# @register.inclusion_tag("templ.html")
# def show_cat():
#     cat = model
#     return {"cat": cat}
