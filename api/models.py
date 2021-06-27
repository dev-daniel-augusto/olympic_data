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
