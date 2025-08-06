from django.contrib import admin
from .models import Item


class MenuItemAdmin(admin.ModelAdmin):
    list_display = ("meal", "status") # what in admin page is shown
    list_filter = ("status",) # filters in the admin page
    search_fields = ("meal", "description")



admin.site.register(Item, MenuItemAdmin)
# Password: Pythoncourse123