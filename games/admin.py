from django.contrib import admin
from games.models import Game, Statistics
# Register your models here.


class GameAdmin(admin.ModelAdmin):
	list_display = ('user', 'game_type', 'create_date', 'modified_date')
	search_fields = ['user', 'game_type', 'id']


class StatisticsAdmin(admin.ModelAdmin):
	list_display = ('game', 'create_date', 'modified_date', 'start_time', 'end_time', 'number_correct', 'number_incorrect')
	search_fields = ['game', 'id']



admin.site.register(Game, GameAdmin)
admin.site.register(Statistics, StatisticsAdmin)