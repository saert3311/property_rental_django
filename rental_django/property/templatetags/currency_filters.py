from django import template

register = template.Library()

@register.filter(name='moneda')
def moneda(value):
    return f"${value:,.2f}"