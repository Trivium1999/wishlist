import list.views as views
from django import template
from ..models import Wish
from django.utils import timezone


register = template.Library()


@register.simple_tag()
def year():
    """Добавляет переменную с текущим годом."""
    year = timezone.now().year
    return year


@register.simple_tag()
def get_wishes():
    return Wish.objects.all()
