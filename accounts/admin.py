from django.contrib import admin

from .models import Permission


class PermissionAdmin(admin.ModelAdmin):
    list_display = ('evnt_name', 'accepted', 'myfile',
                    'description',)
    list_editable = ('accepted', )


admin.site.register(Permission, PermissionAdmin)
