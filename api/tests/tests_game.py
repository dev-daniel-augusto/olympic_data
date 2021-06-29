import requests


class TestGame:
    identifier = 1
    header = {'Authorization': 'Token '}
    url_games = '.../api/v1/games/'

    def test_get_games_success(self):
        response = requests.get(
            url=self.url_games,
            headers=self.header,
        )

        assert response.status_code == 200

    def test_post_game_success(self):
        data = {
            "year": "2035",
            "season": "Summer",
            "city": "City_Name",
            "sport": 4,
            "event": 4,
            "athletes": (5, 4, 3)
        }
        response = requests.post(
            url=self.url_games,
            headers=self.header,
            data=data,
        )

        assert response.status_code == 201

    def test_put_game_success(self):
        data = {
            "year": "2035",
            "season": "Summer",
            "city": "City_Name",
            "sport": 5,
            "event": 5,
            "athletes": (6, 3)
        }
        response = requests.put(
            url=f'{self.url_games}{self.identifier}/',
            headers=self.header,
            data=data,
        )

        assert response.status_code == 200

    def test_delete_game_success(self):
        response = requests.delete(
            url=f'{self.url_games}{self.identifier}/',
            headers=self.header,
        )

        assert response.status_code == 204
