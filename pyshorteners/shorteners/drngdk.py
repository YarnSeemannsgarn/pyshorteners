# encoding: utf-8
"""
drng.dk shortener implementation
No config params needed
"""
from .base import BaseShortener
from ..exceptions import ShorteningErrorException


class DrngdkShortener(BaseShortener):
    api_url = 'http://api.drng.dk/create-link.php'

    def short(self, url):
        params = {
            'url': url,
        }
        response = self._get(self.api_url, params=params)
        if response.ok:
            try:
                data = response.json()
            except ValueError:
                raise ShorteningErrorException('There was an error shortening'
                                               ' this url - {0}'.format(
                                                   response.content))
            return data['link']
        raise ShorteningErrorException('There was an error shortening this '
                                       'url - {0}'.format(response.content))
