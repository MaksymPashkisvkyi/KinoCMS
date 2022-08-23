from django import template

register = template.Library()


@register.inclusion_tag('admin_lte/base/table_buttons.html')
def table_buttons():
    context = []
    return {'context': context}
