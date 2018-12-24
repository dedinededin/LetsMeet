from django import template
from ..models import EventOwner
from django.utils.safestring import mark_safe

register = template.Library()


@register.simple_tag(name='joinbutton')
def joinbuttonmaker(event, profile):
    owner = EventOwner.objects.get(profile=profile)
    for participant in event.participants.all():
        if participant == profile:
            unjoin = '<a href="/event/unjoin/{}">' \
                     '<button id="Button1" class="btn btn-danger">' \
                     '<i class="fas fa-american-sign-language-interpreting fa-lg"></i> Unjoin' \
                     '</button></a>'.format(event.id)
            return mark_safe(unjoin)
    if owner == event.owner:
        return mark_safe("")

    join = '<a href="/event/join/{}">' \
           '<button id="Button1"  class="btn btn-info">' \
           '<i class="fas fa-american-sign-language-interpreting fa-lg"></i> Join' \
           '</button></a>'.format(event.id)

    return mark_safe(join)


@register.simple_tag(name='deletebutton')
def joinbuttonmaker(event, profile):
    owner = EventOwner.objects.get(profile=profile)

    if owner == event.owner:
        join = '<a href="/event/delete/{}">' \
               '<button id="Button1"  class="btn btn-danger">' \
               '<i class="fas fa-trash-alt"></i> Delete' \
               '</button></a>'.format(event.id)
        return mark_safe(join)
    else:
        return mark_safe("")

