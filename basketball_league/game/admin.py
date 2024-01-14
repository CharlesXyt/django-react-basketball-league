from django.contrib import admin

from .models import Game, GamePlayerAssociation, GameTeamAssociation, Round, Tounament

# Register your models here.

admin.site.register(Tounament)
admin.site.register(Round)
admin.site.register(Game)
admin.site.register(GameTeamAssociation)
admin.site.register(GamePlayerAssociation)
