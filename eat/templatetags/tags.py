from django import template
from eat.models import PayFrequency

register = template.Library()


@register.filter(name='getvalue')
def getvalue(object, property):
    if object and property:
        return "" if getattr(object, property) is None else getattr(object, property)
    else:
        return ""


@register.filter(name='frequencylabel')
def frequencylabel(value):
    if value:
        return PayFrequency.objects.get(pk=value)
    else:
        return ""