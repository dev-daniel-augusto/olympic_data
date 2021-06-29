from django.contrib import admin

from .models import (
    Team,
    Sport,
    Event,
    Athlete,
    Game,
    Medal,
)


@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'team_name',
        'noc',
    )
    search_fields = ('team_name', 'noc',)
    list_filter = ('team_name',)


@admin.register(Sport)
class SportAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'sport_name',
    )
    search_fields = ('sport_name',)


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'event_name',
    )
    search_fields = ('event_name',)


@admin.register(Athlete)
class AthleteAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'name',
        'sex',
        'age',
        'height',
        'weight',
        'athlete_team',
        'created',
        'modified',
    )
    search_fields = (
        'name',
        'sex',
        'age',
        'height',
        'weight',
        'athlete_team'
    )
    list_filter = ('sex', 'athlete_team', 'age')


@admin.register(Game)
class Gamedmin(admin.ModelAdmin):
    list_display = (
        'id',
        'year',
        'season',
        'event',
        'sport',
    )
    search_fields = (
        'year',
        'season',
        'event',
        'sport'
    )
    list_filter = ('season', 'sport')


@admin.register(Medal)
class MedalAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'medal',
        'event',
        'winner',
        'created',
        'modified',
    )
    search_fields = ('medal', 'event', 'winner')
    list_filter = ('medal',)
