from account.urls import urlpatterns as account_urls
from django.contrib import admin
from django.urls import path
from game.urls import urlpatterns as game_urls

urlpatterns = [
    path("admin/", admin.site.urls),
] + account_urls + game_urls
