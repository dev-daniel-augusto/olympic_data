from django.db import models


class Core(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Team(Core):
    team_name = models.CharField(max_length=250, unique=True)
    noc = models.CharField(max_length=3)

    class Meta:
        verbose_name = 'Team'
        verbose_name_plural = 'Teams'

    def __str__(self):
        return self.team_name


class Sport(Core):
    sport_name = models.CharField(max_length=200, unique=True)

    class Meta:
        verbose_name = 'Sport'
        verbose_name_plural = 'Sport'

    def __str__(self):
        return self.sport_name


class Event(Core):
    event_name = models.CharField(max_length=255, unique=True)

    class Meta:
        verbose_name = 'Event'
        verbose_name_plural = 'Events'

    def __str__(self):
        return self.event_name


class Athlete(Core):
    name = models.CharField(max_length=250, unique=True)
    sex = models.CharField(max_length=1)
    age = models.IntegerField(default=0)
    height = models.FloatField()
    weight = models.FloatField()
    athlete_team = models.ForeignKey(Team, related_name='athletes', on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Athlete'
        verbose_name_plural = 'Athletes'

    def __str__(self):
        return self.name


class Game(Core):
    year = models.IntegerField()
    season = models.CharField(max_length=6)
    city = models.CharField(max_length=250)
    sport = models.ForeignKey(Sport, related_name='events', on_delete=models.CASCADE)
    event = models.ForeignKey(Event, related_name='games', on_delete=models.CASCADE)
    athletes = models.ManyToManyField(Athlete, related_name='participation')

    class Meta:
        verbose_name = 'Game'
        verbose_name_plural = 'Games'
        unique_together = ['year', 'season', 'event']

    def __str__(self):
        return str(self.event)


class Medal(Core):
    medal = models.CharField(max_length=6, blank=True)
    event = models.ForeignKey(Event, related_name='medals', on_delete=models.CASCADE)
    winner = models.ForeignKey(Athlete, related_name='winners', on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Medal'
        verbose_name_plural = 'Medals'

    def __str__(self):
        return self.medal
