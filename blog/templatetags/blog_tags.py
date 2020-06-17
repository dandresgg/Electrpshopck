from django.utils.safestring import mark_safe
import markdown
from django import template
from ..models import Resistors

register = template.Library()

@register.filter(name='markdown')
def markdown_format(text):
	return mark_safe(markdown.markdown(text))

@register.inclusion_tag('blog/pasive_components.html')
def metalfilm_resistor():
	metalfilm_r = Resistors.objects.all()
	return {'metalfilm_r':metalfilm_r}
