import requests


class TestTeam:
    identifier = 1
    header = {'Authorization': 'Token '}
    url_teams = '.../api/v1/teams/'
    url_teams_error = '.../api/v1/team/'
    url_team_error = '.../api/v1/team/any'

    def test_get_teams_success(self):
        response = requests.get(
            url=self.url_teams,
            headers=self.header,
        )

        assert response.status_code == 200

    def test_get_team_success(self):
        response = requests.get(
            url=f'{self.url_teams}{self.identifier}/',
            headers=self.header,
        )

        assert response.status_code == 200

    def test_get_teams_error(self):
        response = requests.get(
            url=self.url_teams_error,
            headers=self.header,
        )

        assert response.status_code == 404

    def test_get_team_error(self):
        response = requests.get(
            url=self.url_team_error,
            headers=self.header,
        )

        assert response.status_code == 404

    def test_post_team_success(self):
        data = {
            "team_name": "Bullyz",
            "noc": 'BLZ',
        }
        response = requests.post(
            url=self.url_teams,
            headers=self.header,
            data=data,
        )

        assert response.status_code == 201
        assert response.json()['team_name'] == 'Bullyz'
        assert response.json()['team_name'] != 'bullyz'
        assert response.json()['noc'] == 'BLZ'
        assert response.json()['noc'] != 'blz'

    def test_post_team_error(self):
        data = {
            "team_name": "Bullyz",
            "noc": "BLZ",
        }
        response = requests.post(
            url=self.url_teams,
            headers=self.header,
            data=data,
        )

        assert response.status_code == 400

    def test_put_team_success(self):
        data = {
            "team_name": "Ovak",
            "noc": "OVK"
        }
        response = requests.put(
            url=f'{self.url_teams}{self.identifier}/',
            headers=self.header,
            data=data,
        )

        assert response.status_code == 200
        assert response.json()['team_name'] == data['team_name']
        assert response.json()['team_name'] != 'ovak'
        assert response.json()['noc'] != 'ovk'
        assert response.json()['noc'] == data['noc']

    def test_put_team_error_1(self):
        data = {
            "team_name": "Sed ut perspiciatis unde omnis iste natus error sit voluptatem accusantium doloremque "
                         "laudantium, totam rem aperiam eaque ipsa, quae ab illo inventore veritatis et quasi "
                         "architecto beatae vitae dicta sunt, explicabo. Nemo enim ipsam voluptatem, quiaas",
            "noc": "NOC",
        }
        response = requests.put(
            url=self.url_teams,
            headers=self.header,
            data=data
        )

        assert response.status_code == 400

    def test_put_team_error_2(self):
        data = {
            "team_name": "Subplis",
            "noc": "SBPS",
        }
        response = requests.put(
            url=self.url_teams,
            headers=self.header,
            data=data
        )

        assert response.status_code == 400

    def test_delete_team_success(self):
        response = requests.delete(
            url=f'{self.url_teams}{self.identifier}/',
            headers=self.header,
        )

        assert response.status_code == 204

    def test_delete_team_error(self):
        response = requests.delete(
            url=f'{self.url_teams}1346697682134123423492134567/',
            headers=self.header,
        )

        assert response.status_code == 404
