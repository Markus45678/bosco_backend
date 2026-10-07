from store.models import Product
from django import template

register = template.Library()

@register.filter(name='uah')
def uah(value):
    try:
        return f"{float(value):.2f} грн"
    except (ValueError, TypeError):
        return value

@register.simple_tag
def product_count():
    return Product.objects.count()