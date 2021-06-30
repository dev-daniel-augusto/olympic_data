
<h1 align="center">Olympic Data API</h1>

[![REST](https://img.shields.io/badge/framework-django_rest_framework-ff0000?style=flat&logo=Django)](https://www.django-rest-framework.org/) &nbsp;
[![Potgre](https://img.shields.io/badge/database-postgresql-23BCC1?style=flat&logo=PostgreSQL)](https://www.postgresql.org/) &nbsp;
[![Req](https://img.shields.io/badge/requirements-here-23BCC1?style=flat&logo=)](https://github.com/dev-daniel-augusto/olympic_data/blob/master/requirements.txt)



[Live Demo](https://olympic-data-api.herokuapp.com/api/v1/teams/)

## About

This project is an implementation of _120 year of Olympic history: athletes and results_ dataset from Kaggle into an API using Django REST Framework.

The dataset used in this project can be [found here](https://www.kaggle.com/heesoo37/120-years-of-olympic-history-athletes-and-results#athlete_events.csv).

## How to run this project (Ubuntu)

Before cloning the project start a virtual env on your machine to keep the project's dependencies separated (you must have the virtualenv installed on your machine first).

```
virtualenv .env
```
Then active it with:
```
source .env/bin/activate
```
Clone the repository (if any error happens get the repository's link using the code button):
```
git clone https://github.com/dev-daniel-augusto/olympic_data.git
```
Go to the project's directory:
```
cd olympic_data
```
Install all the dependencies running the command bellow:
```
pip install -r requirements.txt
```
Now you must connect to your database inside the settings.py file and fill the SECRET_KEY variable before running the following commands:
```
python manage.py makemigrations
python manage.py migrate
```
## Populating your database with the CSV data 

After doing all the previous steps we can start populating our database using the **athlete_events.csv** file. Open the Django shell with:
```
python manage.py shell
```
There are a few scripts inside [scripts.py](scripts.py) that will help us to put the csv data into our tables. First make sure you're importing all the three first lines of the scripts.py:
```
>>> from django.db import IntegrityError
>>> from csv import reader
>>> from api.models import Team, Sport, Event, Athlete, Game, 
```
After that you can run each python script following this order (the order of the first three scripts does not really matter by the way):

Team Model Script > Sport Model Script > Event Model Script > Athlete Model Script > Game Model Script > Medal Model Script

Eg:

```python
>>> with open('athlete_events.csv') as file:
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
```


## Consuming the API

It won't be possible consuming the data from the live demo website since I won't provide any tokens, just because it's not the project purpose. But once you've configured the project, you can use the command **python manage.py createsuperuser**, go to the admin and add a token to your active profile.

After that you can interact with the API doing something like this:

```python
import requests

header = {'Authorization': 'Token <your_token>'}
url_teams = '.../api/v1/teams/'


def get_url_data(url, headers):
    response = requests.get(url=url_teams, headers=headers)
    if response.status_code == 200:
        return response.json()
    return response.status_code


print(get_url_data(url=url_teams, headers=header))

```


## Possibles URLs

_Make sure you have changed the pk to an int before loading some specific pages._

<table>
    <thead>
        <tr>
            <th>Team</th>
            <th>Sport</th>
            <th>Event</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>
                <ul>
                    <li>https://olympic-data-api.herokuapp.com/api/v1/teams/</li>
                    <li>https://olympic-data-api.herokuapp.com/api/v1/teams/pk/</li>
                    <li>https://olympic-data-api.herokuapp.com/api/v1/teams/pk/athletes/</li>
                </ul>
            </td>
            <td>
                <ul>
                    <li>https://olympic-data-api.herokuapp.com/api/v1/sport/</li>
                    <li>https://olympic-data-api.herokuapp.com/api/v1/sport/pk/events/</li>
                </ul>
            </td>
            <td>
                <ul>
                    <li>https://olympic-data-api.herokuapp.com/api/v1/events/</li>
                    <li>https://olympic-data-api.herokuapp.com/api/v1/events/pk/</li>
                    <li>https://olympic-data-api.herokuapp.com/api/v1/events/pk/medals/</li>
                    <li>https://olympic-data-api.herokuapp.com/api/v1/events/pk/games/</li>
                </ul>
            </td>
        </tr>
    </tbody>
    <thead>
        <tr>
            <th>Athlete</th>
            <th>Game</th>
            <th>Medal</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>
                <ul>
                    <li>https://olympic-data-api.herokuapp.com/api/v1/athletes/</li>
                    <li>https://olympic-data-api.herokuapp.com/api/v1/athletes/pk/</li>
                    <li>https://olympic-data-api.herokuapp.com/api/v1/athletes/pk/achievements/</li>
                    <li>https://olympic-data-api.herokuapp.com/api/v1/athletes/1/games/</li>
                </ul>
            </td>
            <td>
                <ul>
                    <li>https://olympic-data-api.herokuapp.com/api/v1/games/</li>
                    <li>https://olympic-data-api.herokuapp.com/api/v1/games/pk/</li>
                </ul>
            </td>
            <td>
                <ul>
                    <li>https://olympic-data-api.herokuapp.com/api/v1/medals/</li>
                    <li>https://olympic-data-api.herokuapp.com/api/v1/medals/pk/</li>
                </ul>
            </td>
        </tr>
    </tbody>
</table>
