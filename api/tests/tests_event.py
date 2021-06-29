import requests


class TestEvent:
    identifier = 1
    header = {'Authorization': 'Token '}
    url_events = '.../api/v1/events/'

    def test_get_events_success(self):
        response = requests.get(
            url=self.url_events,
            headers=self.header,
        )

        assert response.status_code == 200

    def test_post_event_success(self):
        data = {
            "event_name": "new_event_name",
        }
        response = requests.post(
            url=self.url_events,
            headers=self.header,
            data=data,
        )

        assert response.status_code == 201

    def test_put_event_success(self):
        data = {
            "event_name": "update_event_name"
        }
        response = requests.put(
            url=f'{self.url_events}{self.identifier}/',
            headers=self.header,
            data=data,
        )

        assert response.status_code == 200

    def test_delete_event_success(self):
        response = requests.delete(
            url=f'{self.url_events}{self.identifier}/',
            headers=self.header,
        )

        assert response.status_code == 204
