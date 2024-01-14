from django.contrib import admin

from .models import Account, Role, Team

# Register your models here.

admin.site.register(Account)
admin.site.register(Team)
admin.site.register(Role)
