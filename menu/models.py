from django.db import models


class MenuItem(models.Model):
    title = models.CharField(max_length=50)
    url = models.CharField(max_length=100)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children')
    menu_name = models.CharField(max_length=50)
    view_name = models.CharField(max_length=100, blank=True)
    order = models.IntegerField(default=0)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return self.title
