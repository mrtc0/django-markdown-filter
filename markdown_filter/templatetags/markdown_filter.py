from django import template
from django.conf import settings
import markdown2
import bleach


register = template.Library()


@register.filter
def markdown_filter(text):
    text = markdown2.markdown(text)
    html = bleach.clean(text, tags=settings.MARKDOWN_FILTER_WHITELIST_TAGS)
    return bleach.linkify(html)
