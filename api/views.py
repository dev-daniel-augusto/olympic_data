from rest_framework import viewsets

from django_filters.rest_framework import DjangoFilterBackend


from .models import (
    Team,
    Sport,
    Event,
    Athlete,
    Game,
    Medal,
)
from .serializers import (
    TeamSerializer,
    SportSerializer,
    EventSerializer,
    AthleteSerializer,
    GameSerializer,
    MedalSerializer,
)


class TeamViewSet(viewsets.ModelViewSet):
    queryset = Team.objects.all()
    serializer_class = TeamSerializer
    filter_backends = (DjangoFilterBackend,)
    filterset_fields = (
        'team_name',
        'noc',
        'created',
    )


class SportViewSet(viewsets.ModelViewSet):
    queryset = Sport.objects.all()
    serializer_class = SportSerializer
    filter_backends = (DjangoFilterBackend,)
    filterset_fields = (
        'sport_name',
        'created',
    )


class EventViewSet(viewsets.ModelViewSet):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    filter_backends = (DjangoFilterBackend,)
    filterset_fields = (
        'event_name',
        'created',
    )


class AthleteViewSet(viewsets.ModelViewSet):
    queryset = Athlete.objects.all()
    serializer_class = AthleteSerializer
    filter_backends = (DjangoFilterBackend,)
    filterset_fields = (
        'name',
        'sex',
        'age',
        'height',
        'weight',
        'athlete_team',
        'created',
    )


class GameViewSet(viewsets.ModelViewSet):
    queryset = Game.objects.all()
    serializer_class = GameSerializer
    filter_backends = (DjangoFilterBackend,)
    filterset_fields = (
        'year',
        'season',
        'city',
        'sport',
        'event',
        'athletes',
        'created',
    )


class MedalViewSet(viewsets.ModelViewSet):
    queryset = Medal.objects.all()
    serializer_class = MedalSerializer
    filter_backends = (DjangoFilterBackend,)
    filterset_fields = (
        'medal',
        'event',
        'winner',
        'created',
    )
