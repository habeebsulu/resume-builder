from django import template

register = template.Library()

@register.filter
def filter(query_set, property_name, filter_target):
    if not filter_target:
        return query_set.all()
    property_dict = {property_name: filter_target}
    return query_set.filter(**property_dict)

@register.filter
def profile_filter(query_set, filter_target):
    return filter(query_set, 'profile__name', filter_target)
