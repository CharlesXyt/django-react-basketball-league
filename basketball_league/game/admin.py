from django.contrib import admin

from .models import Game, GamePlayerAssociation, GameTeamAssociation, Round, Tournament

# Register your models here.

admin.site.register(Tournament)
admin.site.register(Round)
admin.site.register(Game)
admin.site.register(GameTeamAssociation)
admin.site.register(GamePlayerAssociation)
