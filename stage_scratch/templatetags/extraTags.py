import re
from django import template
from django.templatetags.static import static


register = template.Library()

@register.filter
def replaceBBCode(value):
    staticPath = static('')
    bbdata = [
        # (r'\[url\](.+?)\[/url\]', r'<a href="\1">\1</a>'),
        # (r'\[url=(.+?)\](.+?)\[/url\]', r'<a href="\1">\2</a>'),
        # (r'\[email\](.+?)\[/email\]', r'<a href="mailto:\1">\1</a>'),
        # (r'\[email=(.+?)\](.+?)\[/email\]', r'<a href="mailto:\1">\2</a>'),
        (r'\[img\](.+?)\[/img\]', r'<img src="'+staticPath+r'\1">'),
        (r'\[img=(.+?)\](.+?)\[/img\]', r'<img src="'+staticPath+r'\1" alt="\2">'),
        # (r'\[b\](.+?)\[/b\]', r'<b>\1</b>'),
        # (r'\[i\](.+?)\[/i\]', r'<i>\1</i>'),
        # (r'\[u\](.+?)\[/u\]', r'<u>\1</u>'),
        # (r'\[quote\](.+?)\[/quote\]', r'<div style="margin-left: 1cm">\1</div>'),
        # (r'\[center\](.+?)\[/center\]', r'<div align="center">\1</div>'),
        # (r'\[code\](.+?)\[/code\]', r'<tt>\1</tt>'),
        # (r'\[big\](.+?)\[/big\]', r'<big>\1</big>'),
        # (r'\[small\](.+?)\[/small\]', r'<small>\1</small>'),
    ]

    # TODO : add BBCode for spoiler image
    
    for bbset in bbdata:
        p = re.compile(bbset[0], re.DOTALL)
        value = p.sub(bbset[1], value)

    return value