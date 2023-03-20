from django import template

register = template.Library()

@register.filter(name='has_role') 
def has_role(user, group_name):
    return user.groups.filter(name=group_name).exists() 