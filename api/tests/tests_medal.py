import requests


class TestMedal:
    identifier = 1
    header = {'Authorization': 'Token '}
    url_medals = '.../api/v1/medals/'

    def test_get_medals_success(self):
        response = requests.get(
            url=self.url_medals,
            headers=self.header,
        )

        assert response.status_code == 200

    def test_post_medal_success(self):
        data = {
            "medal": "gold",
            "event": 1,
            "winner": 34,
        }
        response = requests.post(
            url=self.url_medals,
            headers=self.header,
            data=data,
        )

        assert response.status_code == 201

    def test_put_medal_success(self):
        data = {
            "medal": "gold",
            "event": 1,
            "winner": 34,
        }

        response = requests.put(
            url=f'{self.url_medals}{self.identifier}/',
            headers=self.header,
            data=data,
        )

        assert response.status_code == 200

    def test_delete_medal_success(self):
        response = requests.delete(
            url=f'{self.url_medals}{self.identifier}/',
            headers=self.header,
        )

        assert response.status_code == 204
