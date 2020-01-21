from django import template

register = template.Library()


@register.filter
def cutout(value, arg):
    return value.replace(arg, '')


@register.filter
def caps(value, arg):
    cap = arg.upper()
    return value.replace(arg, cap)
