import requests
from requests_oauthlib import OAuth1


class NetsuiteOauth:
    def __init__(self, url, method, consumer_key, consumer_secret, token_id, token_secret, account):
        self.url = url
        self.method = method
        self.consumer_key = consumer_key
        self.consumer_secret = consumer_secret
        self.token_id = token_id
        self.token_secret = token_secret
        self.account = account
        self.oauth = OAuth1(
            consumer_key,
            client_secret=consumer_secret,
            resource_owner_key=token_id,
            resource_owner_secret=token_secret,
            realm=account, signature_method='HMAC-SHA256',
            signature_type='AUTH_HEADER'
        )

    def get(self):
        headers = {'Content-Type': 'application/json'}
        response = requests.get(self.url, auth=self.oauth, headers=headers)
        response.raise_for_status()
        return response

    def post(self, data):
        headers = {'Content-Type': 'application/json'}
        response = requests.post(self.url, json=data, auth=self.oauth, headers=headers)
        response.raise_for_status()
        return response
