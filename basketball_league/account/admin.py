from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as DefaultUserAdmin

from .models import Account, Role, Team


class UserAdmin(DefaultUserAdmin):
    pass


admin.site.register(Account, UserAdmin)
admin.site.register(Team)
admin.site.register(Role)
