from django.contrib import admin
from .models import Game
class GameAdmin(admin.ModelAdmin):
    list_display = ('name', 'cover', 'active')
    prepopulated_fields = {'slug': ('name',)}

admin.site.register(Game, GameAdmin)