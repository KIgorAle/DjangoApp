from django import forms
from .models import MenuItem


class MenuItemForm(forms.ModelForm):
    class Meta:
        model = MenuItem
        fields = ('title', 'url', 'parent', 'menu_name', 'order')
