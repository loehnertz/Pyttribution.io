import logging
import json
import random
import string
import time

import requests
from requests import RequestException

logger = logging.getLogger(__name__)


class PyttributionIo:
    GET_REQUEST = 'GET'
    API_URL = 'https://attribution.io/api/v1'

    def __init__(self, api_key, api_secret):
        self._api_key = api_key
        self._api_secret = api_secret

    """
    General methods
    """

    def _send_private_api_request(self, subject_id, method='GET', endpoint='customers', **params):
        response = requests.request(
            method=method,
            url=f'{PyttributionIo.API_URL}/{self._api_key}/{endpoint}/{subject_id}',
            params={
                **{'secret': self._api_secret},
                **params
            },
        )

        if not response.ok:
            raise RequestException(response.text)

        return json.loads(response.content)
