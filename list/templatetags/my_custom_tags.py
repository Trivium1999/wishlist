from django import template
from ..models import Wish


register = template.Library()

@register.simple_tag()
def get_wishes():
    return Wish.objects.all()
