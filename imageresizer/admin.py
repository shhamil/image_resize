from django.contrib import admin
from .models import Pikcha


@admin.register(Pikcha)
class ImageAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'url', 'picture')
    list_filter = ('name', 'width', 'height')
    search_fields = ('name', 'width', 'height')
