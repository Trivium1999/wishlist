from django.contrib import admin

from .models import Wish


@admin.register(Wish)
class WishAdmin(admin.ModelAdmin):
    list_display = ('pk', 'title', 'description', 'pub_date', 'gift')
    list_display_links = ('title',)
    search_fields = ('title',)
    list_editable = ('gift',)
    prepopulated_fields = {"slug": ("title",)}
    empty_value_display = '-пусто-'
