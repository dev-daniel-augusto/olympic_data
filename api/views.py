from rest_framework import viewsets

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


class SportViewSet(viewsets.ModelViewSet):
    queryset = Sport.objects.all()
    serializer_class = SportSerializer


class EventViewSet(viewsets.ModelViewSet):
    queryset = Event.objects.all()
    serializer_class = EventSerializer


class AthleteViewSet(viewsets.ModelViewSet):
    queryset = Athlete.objects.all()
    serializer_class = AthleteSerializer


class GameViewSet(viewsets.ModelViewSet):
    queryset = Game.objects.all()
    serializer_class = GameSerializer


class MedalViewSet(viewsets.ModelViewSet):
    queryset = Medal.objects.all()
    serializer_class = MedalSerializer
