from rest_framework.response import Response
from rest_framework.decorators import action
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

    @action(detail=True, methods=['get', 'post', 'delete'])
    def athletes(self, request, pk=None):
        team = self.get_object()
        serializer_athletes = AthleteSerializer(team.athletes.all(), many=True)
        return Response(serializer_athletes.data)


class SportViewSet(viewsets.ModelViewSet):
    queryset = Sport.objects.all()
    serializer_class = SportSerializer
    filter_backends = (DjangoFilterBackend,)
    filterset_fields = (
        'sport_name',
        'created',
    )

    @action(detail=True, methods=['get', 'post', 'delete'])
    def events(self, request, pk=None):
        sport = self.get_object()
        serializer_events = GameSerializer(sport.events.all(), many=True)
        return Response(serializer_events.data)


class EventViewSet(viewsets.ModelViewSet):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    filter_backends = (DjangoFilterBackend,)
    filterset_fields = (
        'event_name',
        'created',
    )

    @action(detail=True, methods=['get', 'post', 'delete'])
    def medals(self, request, pk=None):
        event = self.get_object()
        serializer_medals = MedalSerializer(event.medals.all(), many=True)
        return Response(serializer_medals.data)

    @action(detail=True, methods=['get', 'post', 'delete'])
    def games(self, request, pk=None):
        event = self.get_object()
        serializer_games = GameSerializer(event.games.all(), many=True)
        return Response(serializer_games.data)


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

    @action(detail=True, methods=['get', 'posts'])
    def achievements(self, request, pk=None):
        athlete = self.get_object()
        serializer_winners = MedalSerializer(athlete.winners.all(), many=True)
        return Response(serializer_winners.data)

    @action(detail=True, methods=['get', 'posts'])
    def games(self, request, pk=None):
        athlete = self.get_object()
        serializer_games = GameSerializer(athlete.participation.all(), many=True)
        return Response(serializer_games.data)


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
