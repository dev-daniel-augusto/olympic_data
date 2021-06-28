from rest_framework import serializers

from .models import (
    Team,
    Sport,
    Event,
    Athlete,
    Game,
    Medal,
    )


class TeamSerializer(serializers.ModelSerializer):

    class Meta:
        model = Team
        fields = (
            'id',
            'team_name',
            'noc',
        )


class SportSerializer(serializers.ModelSerializer):

    class Meta:
        model = Sport
        fields = (
            'id',
            'sport_name',
        )


class EventSerializer(serializers.ModelSerializer):

    class Meta:
        model = Event
        fields = (
            'id',
            'event_name',
        )


class AthleteSerializer(serializers.ModelSerializer):

    class Meta:
        model = Athlete
        fields = (
            'id',
            'name',
            'sex',
            'age',
            'height',
            'weight',
            'athlete_team',
        )


class GameSerializer(serializers.ModelSerializer):

    class Meta:
        model = Game
        fields = (
            'year',
            'season',
            'city',
            'sport',
            'event',
            'athletes',
        )


class MedalSerializer(serializers.ModelSerializer):

    class Meta:
        model = Medal
        fields = (
            'medal',
            'event',
            'winner',
        )
