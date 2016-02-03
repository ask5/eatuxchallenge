from django import template

register = template.Library()


@register.inclusion_tag('eat/user/application/nav.html')
def show_nav(nav):
    return {'nav': nav}