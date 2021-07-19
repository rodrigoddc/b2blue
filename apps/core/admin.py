from django.contrib import admin


class GaleryAdmin(admin.ModelAdmin):
    list_display = ("__str__", )
