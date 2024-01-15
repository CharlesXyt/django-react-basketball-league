from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as DefaultUserAdmin

from .models import Account, Role, Team

admin.site.register(Account)
admin.site.register(Team)
admin.site.register(Role)
