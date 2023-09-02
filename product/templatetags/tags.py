from django import template

from product.models import Category

register = template.Library()

# @register.simple_tag('add')
# def add(value,v1):
#     return value + v1



#
# @register.simple_tag('get_category_list')
# def get_category_list(cats):
#     return Category.objects.all()