from django.db import IntegrityError

from csv import reader

from api.models import Team, Sport, Event, Athlete, Game, Medal


# Team Model Script
with open('athlete_events.csv') as file:
    identifier = 1
    csv_reader = reader(file)
    next(csv_reader)  # Skipping the header
    for row in csv_reader:
        try:
            team = Team.objects.create(
                id=identifier,
                team_name=row[6],
                noc=row[7],
                )
            try:
                team.save()
                identifier = identifier + 1
            except Exception:
                pass
        except IntegrityError:
            pass


# Sport Model Script
with open('athlete_events.csv') as file:
    identifier = 1
    csv_reader = reader(file)
    next(csv_reader)
    for row in csv_reader:
        try:
            sport = Sport.objects.create(
                id=identifier,
                sport_name=row[12],
            )
            try:
                sport.save()
                identifier = identifier + 1
            except Exception:
                pass
        except IntegrityError:
            pass


# Event Model Script
with open('athlete_events.csv') as file:
    identifier = 1
    csv_reader = reader(file)
    next(csv_reader)
    for row in csv_reader:
        try:
            event = Event.objects.create(
                id=identifier,
                event_name=row[13],
            )
            try:
                event.save()
                identifier = identifier + 1
            except Exception:
                pass
        except IntegrityError:
            pass


# Athlete Model Script
with open('athlete_events.csv') as file:
    identifier = 1
    csv_reader = reader(file)
    next(csv_reader)
    for row in csv_reader:
        try:
            team = Team.objects.get(team_name=row[6])
            team_id = team.id

            age = row[3]
            height = row[4]
            weight = row[5]

            if age == 'NA':
                age = 0
            if height == 'NA':
                height = 0
            if weight == 'NA':
                weight = 0

            athlete = Athlete.objects.create(
                id=identifier,
                name=row[1],
                sex=row[2],
                age=age,
                height=height,
                weight=weight,
                athlete_team_id=team_id,
            )
            try:
                athlete.save()
                identifier = identifier + 1
            except Exception:
                pass
        except (Team.DoesNotExist, IntegrityError):
            pass


# Game Model Script
with open('athlete_events.csv') as file:
    identifier =  1
    csv_reader = reader(file)
    next(csv_reader)
    for row in csv_reader:
        try:
            event = Event.objects.get(event_name=row[13])
            event_id = event.id
            game = Game.objects.get(
                year=row[9],
                season=row[10],
                event=event_id,
            )
            try:
                athlete = Athlete.objects.get(name=row[1])
                athlete_id = athlete.id
                game.athletes.add(athlete_id)
                game.save()
            except (Athlete.DoesNotExist, IntegrityError):
                pass
        except Game.DoesNotExist:
            event = Event.objects.get(event_name=row[13])
            event_id = event.id
            sport = Sport.objects.get(sport_name=row[12])
            sport_id = sport.id
            game = Game.objects.create(
                id=identifier,
                year=row[9],
                season=row[10],
                city=row[11],
                sport_id=sport_id,
                event_id=event_id,
            )
            try:
                athlete = Athlete.objects.get(name=row[1])
                athlete_id = athlete.id
                game.athletes.add(athlete_id)
                try:
                    game.save()
                    identifier = identifier + 1
                except Exception:
                    pass
            except (Athlete.DoesNotExist, IntegrityError):
                pass


# Medal Model Script
with open('athlete_events.csv') as file:
    identifier = 1
    csv_reader = reader(file)
    next(csv_reader)
    for row in csv_reader:
        if row[14] != 'NA':
            try:
                winner = Athlete.objects.get(name=row[1])
                winner_id = winner.id

                event = Event.objects.get(event_name=row[13])
                event_id = event.id

                medal = Medal.objects.create(
                    id=identifier,
                    medal=row[14],
                    event_id=event_id,
                    winner_id=winner_id
                )
                try:
                    medal.save()
                    identifier = identifier + 1
                except Exception:
                    pass
            except Exception:
                pass
