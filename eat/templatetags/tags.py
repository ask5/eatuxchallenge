from django import template
from eat.models import PAY_FREQUENCIES

register = template.Library()


@register.filter(name='getvalue')
def getvalue(object, property):
    if object:
        return getattr(object, property)
    else:
        return None

@register.filter(name='frequencylabel')
def frequencylabel(value):
    if value:
        return dict(PAY_FREQUENCIES).get(value)
    else:
        return ""