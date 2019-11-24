# django-markdown-filter

# Usage

```
{% load markdown_filter %}
{{ model|markdown_filter|safe }}
```

See example.

# Install

```
pip install django-markdown-filter
```

To enable dajngo-markdown-filter in your project you need to add it to INSTALLED_APPS in your projects settings.py file:
```
INSTALLED_APPS = [
    ...
    'markdown_filter',
    ...
]
```

Add whitelist HTML tags to your projects settings.py file:
```
MARKDOWN_FILTER_WHITELIST_TAGS = [
    'a',
    'p',
    'code',
    'h1',
]

```
