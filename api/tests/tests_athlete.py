import requests


class TestAthlete:
    identifier = 1
    header = {'Authorization': 'Token '}
    url_athletes = '.../api/v1/athletes/'

    def test_get_athletes_success(self):
        response = requests.get(
            url=self.url_athletes,
            headers=self.header,
        )

        assert response.status_code == 200

    def test_post_athlete_success(self):
        data = {
            "name": "Athlete",
            "sex": "F",
            "age": 38,
            "height": 180.0,
            "weight": 180.0,
            "athlete_team": 1,
        }
        response = requests.post(
            url=self.url_athletes,
            headers=self.header,
            data=data,
        )

        assert response.status_code == 201

    def test_put_athlete_success(self):
        data = {
            "name": "New_Athlete_Name",
            "sex": "M",
            "age": 83,
            "height": 180.0,
            "weight": 180.0,
            "athlete_team": 2,
        }
        response = requests.put(
            url=f'{self.url_athletes}{self.identifier}/',
            headers=self.header,
            data=data,
        )

        assert response.status_code == 200

    def test_delete_athlete_success(self):
        response = requests.delete(
            url=f'{self.url_athletes}{self.identifier}/',
            headers=self.header,
        )

        assert response.status_code == 204
