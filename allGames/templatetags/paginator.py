import os
from django import template

register = template.Library()

@register.filter(name='page_count')
def page_count(for_counter, page_num):
    if page_num != 1:
        return (page_num - 1) * 20 + for_counter

    return for_counter
