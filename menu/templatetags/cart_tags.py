from django import template


register = template.Library()


@register.filter
def dict_total_quantity(cart):
    if not cart:
        return 0
    return sum(item.get("quantity", 0) for item in cart.values())


@register.filter
def multiply(value, arg):
    return value * arg
