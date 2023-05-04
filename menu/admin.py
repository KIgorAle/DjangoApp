from django.contrib import admin
from .models import MenuItem
from .forms import MenuItemForm


class MenuItemAdmin(admin.ModelAdmin):
    form = MenuItemForm
    list_display = ('title', 'parent', 'menu_name', 'order')
    list_editable = ('order',)


admin.site.register(MenuItem, MenuItemAdmin)
