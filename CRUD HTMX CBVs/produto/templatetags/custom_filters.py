from django import template

register = template.Library()

@register.filter(name='replace_comma')
def replace_comma(value):
    """
    Filtro customizado para substituir vírgulas por pontos em valores numéricos.
    """
    if isinstance(value, str):
        return value.replace(',', '.')
    return value
