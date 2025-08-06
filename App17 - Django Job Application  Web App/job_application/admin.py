from django.contrib import admin
from .models import Form # import the database
# Admin auto-created page!


class FormAdmin(admin.ModelAdmin): # Customize the admin page
    list_display = ("first_name", "last_name", "email", "date")
    search_fields = ("first_name", "last_name", "email", "date")
    list_filter = ("date", "occupation")
    ordering = ("first_name", "last_name", "date")
    readonly_fields = ("occupation", )


admin.site.register(Form, FormAdmin)
# Password: Pythoncourse123

