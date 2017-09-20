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

    """
    Private API methods
    """

    """
    Section: Customer
    """

    def fetch_customer_info_base(self, client_id):
        try:
            return self._send_private_api_request(
                method=PyttributionIo.GET_REQUEST,
                endpoint='customers',
                subject_id=client_id,
            ).get('customer')
        except RequestException as e:
            logger.error(f'Retrieval of base customer info failed with HTTP status {e}')

    def fetch_customer_info_full(self, client_id):
        try:
            return self._send_private_api_request(
                method=PyttributionIo.GET_REQUEST,
                endpoint='customers',
                subject_id=client_id,
                show_all='true'
            ).get('customer')
        except RequestException as e:
            logger.error(f'Retrieval of full customer info failed with HTTP status {e}')
