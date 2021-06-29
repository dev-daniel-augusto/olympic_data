import requests


class TestSport:
    identifier = 1
    header = {'Authorization': 'Token '}
    url_sport = '.../api/v1/sport/'

    def test_get_sport_success(self):
        response = requests.get(
            url=self.url_sport,
            headers=self.header,
        )

        assert response.status_code == 200

    def test_post_sport_success(self):
        data = {
            "sport_name": "new_sport_name",
        }
        response = requests.post(
            url=self.url_sport,
            headers=self.header,
            data=data,
        )

        assert response.status_code == 201

    def test_put_sport_success(self):
        data = {
            "sport_name": "update_sport_name"
        }
        response = requests.put(
            url=f'{self.url_sport}{self.identifier}/',
            headers=self.header,
            data=data,
        )

        assert response.status_code == 200

    def test_delete_sport_success(self):
        response = requests.delete(
            url=f'{self.url_sport}{self.identifier}/',
            headers=self.header,
        )

        assert response.status_code == 204
