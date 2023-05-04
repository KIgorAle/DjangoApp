from django import template
from django.urls import reverse
from django.utils.safestring import SafeText

from menu.models import MenuItem

register = template.Library()


@register.simple_tag(takes_context=True)
def draw_menu(context, menu_name):
    request = context['request']
    current_url = request.path

    menu_items = MenuItem.objects.filter(menu_name=menu_name).select_related('parent').order_by('order')

    def get_parents(item):
        parents = []
        while item.parent:
            parents.append(item.parent)
            item = item.parent
        return parents

    def process_menu_items(parent, level=0, processed_items=None):
        if processed_items is None:
            processed_items = set()
        if parent in processed_items:
            return
        processed_items.add(parent)

        children = parent.children.all()
        if children:
            display = False
            for child in children:
                if child.url:
                    if current_url.startswith(child.url):
                        display = True
                        break
                else:
                    if process_menu_items(child, level + 1, processed_items):
                        display = True
                        break

            if active_item and parent in get_parents(active_item):
                display = True

            if parent == active_item or (active_item and parent == active_item.parent):
                display = True

            yield '<ul{}>'.format(' style="display:block;"' if display else ' style="display:none;"')
            for child in children:
                if child.url:
                    url = child.url
                else:
                    url = reverse(child.view_name)
                active = current_url == url or current_url.startswith(url)
                yield '<li{}>'.format(' class="active"' if active else '')
                yield '<a href="{}">{}</a>'.format(url, child.title)
                yield from process_menu_items(child, level + 1, processed_items)
                yield '</li>'
            yield '</ul>'
        else:
            yield ''

    result = []
    active_item = menu_items.filter(url=current_url).first()

    for item in menu_items.filter(parent=None):
        if item.url:
            url = item.url
        elif item.view_name:
            url = reverse(item.view_name)
        else:
            url = ''
        active = current_url == url or current_url.startswith(url)
        result.append('<li{}>'.format(' class="active"' if active else ''))
        result.append('<a href="{}">{}</a>'.format(url, item.title))
        result.extend(process_menu_items(item))
        result.append('</li>')
    return SafeText(''.join(result))
