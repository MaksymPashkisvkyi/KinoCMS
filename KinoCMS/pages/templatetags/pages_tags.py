from django import template

register = template.Library()


@register.inclusion_tag('pages/navbar.html')
def navbar():
    menu = []
    return {'menu': menu}


@register.inclusion_tag('pages/social_media_icons.html')
def social_media_icons():
    icons = []
    return {'icons': icons}
