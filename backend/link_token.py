import falcon

from plaid import Client

from backend.backend_utils import validate_params


class LinkToken:
    def __init__(self, client: Client):
        self.client = client

    def on_get(self, req, resp):
        validate_params(req.params, 'user_id')
        response = self.client.LinkToken.create({
            'user': {
                'client_user_id': 'test_user',
            },
            'products': ["transactions"],
            'client_name': "My App",
            'country_codes': ['US'],
            'language': 'en',
        })
        resp.body = response['link_token']
